// src/assets/ZodiacContainer.jsx
import React from 'react';
import './ZodiacContainer.css';

function ZodiacContainer({ sign, coverImage, onClick }) {
  return (
    <div className="zodiac-container" onClick={onClick}>
      <img src={coverImage} alt={sign} className="zodiac-image" />
      <p className="zodiac-name">{sign}</p>
    </div>
  );
}

export default ZodiacContainer;
