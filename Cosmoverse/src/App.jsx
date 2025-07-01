import React, { useState } from 'react';
import ZodiacContainer from './assets/ZodiacContainer.jsx';
import zodiacData from './assets/zodiacData.js';
import './App.css'; // Updated styles

function App() {
  const [selectedSign, setSelectedSign] = useState(null);

  const handleSignClick = (sign) => {
    setSelectedSign(sign);
  };

  const handleBackClick = () => {
    setSelectedSign(null);
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>COSMOVERSE</h1>
        <nav>
          <a href="#horoscope">Horoscope</a>
          <a href="#zodiac-sign">Zodiac Sign</a>
          <a href="#about-us">About Us</a>
        </nav>
      </header>
      {selectedSign ? (
        <div className="details-container">
          <h2>{selectedSign.sign}</h2>
          <img src={selectedSign.coverImage} alt={selectedSign.sign} className="zodiac-image" />
          <p>{selectedSign.details}</p>
          <div className="button-container">
            <button className="back-button" onClick={handleBackClick}>Back</button>
            <button className="share-button">Share</button>
          </div>
        </div>
      ) : (
        <div className="zodiac-grid">
          {zodiacData.map((zodiac, index) => (
            <ZodiacContainer
              key={index}
              sign={zodiac.sign}
              coverImage={zodiac.coverImage}
              onClick={() => handleSignClick(zodiac)}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
