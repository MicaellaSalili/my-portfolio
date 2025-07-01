// src/components/ZodiacSignPage.jsx
import React from 'react';
import { useParams } from 'react-router-dom';
import zodiacData from '../assets/zodiacData';

const ZodiacSignPage = () => {
  const { sign } = useParams();
  const zodiac = zodiacData.find(z => z.sign === sign);

  if (!zodiac) {
    return <div>Sign not found</div>;
  }

  return (
    <div className="zodiac-details">
      <h2>{zodiac.sign}</h2>
      <p>{zodiac.details}</p>
      <button onClick={() => window.alert('Shared!')}>Share</button>
    </div>
  );
};

export default ZodiacSignPage;
