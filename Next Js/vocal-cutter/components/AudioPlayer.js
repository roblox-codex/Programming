// /components/AudioPlayer.js
import React from 'react';

export default function AudioPlayer({ src }) {
  return (
    <audio controls style={{ width: '100%' }}>
      <source src={src} type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  );
}
