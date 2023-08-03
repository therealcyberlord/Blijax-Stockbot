import { useState } from "react";

const Stockbot = () => {
  const [inputValue, setInputValue] = useState("");
  const [displayValue, setDisplayValue] = useState("");

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleEnterPress = (event) => {
    if (event.key === "Enter") {
      // set the display value and clear the input value
      setDisplayValue(inputValue);
      setInputValue("");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <div className="absolute top-24 bg-gray-400 p-6 rounded-lg w-5/6 h-2/3">
        <div className="bg-gray-400 p-6 rounded-lg w-full h-full">
          <h3 className="text-gray">{displayValue}</h3>
        </div>
      </div>
      <div className="absolute bottom-4 bg-gray-400 p-6 rounded-lg w-5/6">
        <input
          type="text"
          className="w-full bg-white border border-gray-400 rounded px-4 py-2 mt-2"
          placeholder="Type here..."
          value={inputValue}
          onChange={handleInputChange}
          onKeyDown={handleEnterPress}
        />
      </div>
    </div>
  );
};

export default Stockbot;
