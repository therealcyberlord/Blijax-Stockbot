// eslint-disable-next-line no-unused-vars
import React, { useState } from 'react';

const Stockbot = () => {
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    if (event.keyCode === 13) { // Check if Enter key is pressed
      setInputValue(event.target.value);
      event.target.value = ''; // Clear the text box after Enter is pressed
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <div className="absolute top-24 bg-gray-400 p-6 rounded-lg w-5/6 h-2/3">
        <div className="bg-gray-400 p-6 rounded-lg w-full h-full">
          <h3>{inputValue}</h3>
        </div>
      </div>
      <div className="absolute bottom-4 bg-gray-400 p-6 rounded-lg w-5/6">
        <input
          type="text"
          className="w-full bg-white border border-gray-400 rounded px-4 py-2 mt-2"
          placeholder="Type here..."
          onKeyDown={handleInputChange}
        />
      </div>
    </div>
  );
};

export default Stockbot;

