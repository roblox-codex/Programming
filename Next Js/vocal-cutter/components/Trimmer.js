// /components/Trimmer.js
import React, { useState, useRef, useEffect } from 'react';
import { Button, TextField, Box } from '@mui/material';
import WaveformVisualizer from './WaveformVisualizer';

export default function Trimmer({ src }) {
  const [audioBuffer, setAudioBuffer] = useState(null);
  const [startTime, setStartTime] = useState(0);
  const [endTime, setEndTime] = useState(0);
  const [trimmedAudioURL, setTrimmedAudioURL] = useState(null);
  const audioContextRef = useRef(new (window.AudioContext || window.webkitAudioContext)());

  useEffect(() => {
    const loadAudio = async () => {
      if (!src) return;
      const response = await fetch(src);
      const audioData = await response.arrayBuffer();
      const audioBuffer = await audioContextRef.current.decodeAudioData(audioData);
      setAudioBuffer(audioBuffer);
      setEndTime(audioBuffer.duration);
    };
    loadAudio();
  }, [src]);

  const handleTrim = () => {
    if (!audioBuffer) return;

    const startOffset = Math.floor(startTime * audioBuffer.sampleRate);
    const endOffset = Math.floor(endTime * audioBuffer.sampleRate);
    const trimmedBuffer = audioContextRef.current.createBuffer(
      audioBuffer.numberOfChannels,
      endOffset - startOffset,
      audioBuffer.sampleRate
    );

    for (let channel = 0; channel < audioBuffer.numberOfChannels; channel++) {
      const channelData = audioBuffer
        .getChannelData(channel)
        .slice(startOffset, endOffset);
      trimmedBuffer.copyToChannel(channelData, channel, 0);
    }

    const trimmedBlob = bufferToWave(trimmedBuffer);
    const url = URL.createObjectURL(trimmedBlob);
    setTrimmedAudioURL(url);
  };

  const bufferToWave = (abuffer) => {
    let numOfChan = abuffer.numberOfChannels,
      length = abuffer.length * numOfChan * 2 + 44,
      buffer = new ArrayBuffer(length),
      view = new DataView(buffer),
      channels = [],
      i,
      sample,
      offset = 0,
      pos = 0;

    setUint32(0x46464952); // "RIFF"
    setUint32(length - 8); // file length - 8
    setUint32(0x45564157); // "WAVE"

    setUint32(0x20746d66); // "fmt " chunk
    setUint32(16); // length = 16
    setUint16(1); // PCM (uncompressed)
    setUint16(numOfChan);
    setUint32(abuffer.sampleRate);
    setUint32(abuffer.sampleRate * 2 * numOfChan); // avg. bytes/sec
    setUint16(numOfChan * 2); // block-align
    setUint16(16); // 16-bit (hardcoded in this demo)

    setUint32(0x61746164); // "data" - chunk
    setUint32(length - pos - 4); // chunk length

    for (i = 0; i < abuffer.numberOfChannels; i++)
      channels.push(abuffer.getChannelData(i));

    while (pos < length) {
      for (i = 0; i < numOfChan; i++) {
        sample = Math.max(-1, Math.min(1, channels[i][offset])); // clamp
        sample = sample < 0 ? sample * 0x8000 : sample * 0x7fff; // scale to 16-bit signed int
        view.setInt16(pos, sample, true); // write 16-bit sample
        pos += 2;
      }
      offset++; // next source sample
    }

    return new Blob([buffer], { type: 'audio/wav' });

    function setUint16(data) {
      view.setUint16(pos, data, true);
      pos += 2;
    }

    function setUint32(data) {
      view.setUint32(pos, data, true);
      pos += 4;
    }
  };

  const handleListen = () => {
    if (!audioBuffer) return;

    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const startOffset = Math.floor(startTime * audioBuffer.sampleRate);
    const endOffset = Math.floor(endTime * audioBuffer.sampleRate);
    const trimmedBuffer = audioContext.createBuffer(
      audioBuffer.numberOfChannels,
      endOffset - startOffset,
      audioBuffer.sampleRate
    );

    for (let channel = 0; channel < audioBuffer.numberOfChannels; channel++) {
      const channelData = audioBuffer
        .getChannelData(channel)
        .slice(startOffset, endOffset);
      trimmedBuffer.copyToChannel(channelData, channel, 0);
    }

    const source = audioContext.createBufferSource();
    source.buffer = trimmedBuffer;
    source.connect(audioContext.destination);
    source.start();
  };

  const handleDownload = () => {
    if (trimmedAudioURL) {
      const link = document.createElement('a');
      link.href = trimmedAudioURL;
      link.download = 'trimmed-audio.wav';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };

  return (
    <div>
      <WaveformVisualizer audioBuffer={audioBuffer} setStartTime={setStartTime} setEndTime={setEndTime} />
      <Box display="flex" alignItems="center">
        <TextField
          label="Start Time (seconds)"
          type="number"
          value={startTime}
          onChange={(e) => setStartTime(e.target.value)}
          inputProps={{ min: 0, step: 0.1 }}
        />
        <TextField
          label="End Time (seconds)"
          type="number"
          value={endTime}
          onChange={(e) => setEndTime(e.target.value)}
          inputProps={{ min: 0, step: 0.1 }}
        />
        <Button variant="contained" color="primary" onClick={handleTrim} style={{ marginLeft: '10px' }}>
          Trim
        </Button>
        <Button variant="contained" color="primary" onClick={handleListen} style={{ marginLeft: '10px' }}>
          Listen
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={handleDownload}
          style={{ marginLeft: '10px' }}
          disabled={!trimmedAudioURL}
        >
          Download
        </Button>
      </Box>
    </div>
  );
}
