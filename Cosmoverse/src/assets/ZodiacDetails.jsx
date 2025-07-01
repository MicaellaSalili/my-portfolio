// src/assets/ZodiacDetails.jsx
import React from 'react';
import ShareButton from './ShareButton.jsx';

function ZodiacDetails({ sign, details }) {
  return (
    <div className="zodiac-details">
      <h2>{sign}</h2>
      <p>{details}</p>
      <ShareButton />
    </div>
  );
}

export default ZodiacDetails;
