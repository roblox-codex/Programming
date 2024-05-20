// /pages/index.js
import Head from 'next/head';
import { useState } from 'react';
import { Container, Typography, Box } from '@mui/material';
import FileUploader from '../components/FileUploader';
import AudioPlayer from '../components/AudioPlayer';
import Trimmer from '../components/Trimmer';

export default function Home() {
  const [audioSrc, setAudioSrc] = useState(null);

  return (
    <div>
      <Head>
        <title>Vocal Cutter</title>
        <meta name="description" content="A simple vocal cutter tool" />
      </Head>
      <Container>
        <Typography variant="h2" gutterBottom>
          Vocal Cutter
        </Typography>
        <FileUploader setAudioSrc={setAudioSrc} />
        {audioSrc && (
          <Box mt={4}>
            <AudioPlayer src={audioSrc} />
            <Trimmer src={audioSrc} />
          </Box>
        )}
      </Container>
    </div>
  );
}
