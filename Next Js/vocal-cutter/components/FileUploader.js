// /components/FileUploader.js
import { Button } from '@mui/material';

export default function FileUploader({ setAudioSrc }) {
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const objectUrl = URL.createObjectURL(file);
      setAudioSrc(objectUrl);
    }
  };

  return (
    <div>
      <input
        accept="audio/*"
        style={{ display: 'none' }}
        id="upload-button"
        type="file"
        onChange={handleFileChange}
      />
      <label htmlFor="upload-button">
        <Button variant="contained" component="span">
          Upload Audio
        </Button>
      </label>
    </div>
  );
}
