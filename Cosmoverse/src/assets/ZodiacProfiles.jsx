// src/components/ZodiacProfiles.jsx
import React from 'react';
import zodiacData from '../assets/zodiacData';
import { useNavigate } from 'react-router-dom';

const ZodiacProfiles = () => {
  const navigate = useNavigate();

  const handleClick = (sign) => {
    navigate(`/zodiac/${sign}`);
  };

  return (
    <div className="zodiac-grid">
      {zodiacData.map((zodiac, index) => (
        <div key={index} className="zodiac-container" onClick={() => handleClick(zodiac.sign)}>
          <img src={zodiac.coverImage} alt={zodiac.sign} />
          <h2>{zodiac.sign}</h2>
          <p>{zodiac.description}</p>
        </div>
      ))}
    </div>
  );
};

export default ZodiacProfiles;

