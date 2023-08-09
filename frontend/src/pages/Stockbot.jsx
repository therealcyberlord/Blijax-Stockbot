import { useState, useRef, useEffect } from "react";

const getBot = (prompt) => {
  const url = "http://localhost:8000" + "/generate/";
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: prompt,
    }),
  };
  return fetch(url, options).then((res) => res.json());
};

const Stockbot = () => {
  const [messageHistory, setMessageHistory] = useState([]); // New state for message history
  const inputRef = useRef(null);

  const handleInputChange = async (event) => {
    if (event.keyCode === 13) {
      const newMessage = event.target.value;
      const userMessage = { text: newMessage, isUser: true };
      setMessageHistory((prevHistory) => [...prevHistory, userMessage]);

      event.target.value = "";

      try {
        const botResponse = await getBot(newMessage);
        const botMessage = { text: botResponse, isUser: false };
        setMessageHistory((prevHistory) => [...prevHistory, botMessage]);
      } catch (error) {
        const errorMessage = error.message;
        const errorBotMessage = { text: errorMessage, isUser: false };
        setMessageHistory((prevHistory) => [...prevHistory, errorBotMessage]);
      }
    }
  };

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <div className="absolute top-24 bg-blue-300 p-6 rounded-lg w-5/6 h-2/3">
        <div className="bg-blue-300 p-6 rounded-lg w-full h-full overflow-y-scroll">
          {messageHistory.map((message, index) => (
            <div
              key={index}
              className={`mb-2 ${message.isUser ? "text-right" : "text-left"}`}
            >
              <div
                className={`${
                  message.isUser ? "bg-blue-500 text-white" : "bg-white"
                } inline-block px-4 py-2 rounded-lg`}
                style={{ font: "Arial, sans-serif", fontSize: "16px" }} // You can adjust font and fontSize here
              >
                {message.text}
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="absolute bottom-4 bg-blue-300 p-6 rounded-lg w-5/6">
        <input
          ref={inputRef}
          type="text"
          className="w-full bg-white border border-blue-300 rounded px-4 py-2 mt-2"
          placeholder="Type here..."
          onKeyDown={handleInputChange}
        />
      </div>
    </div>
  );
};

export default Stockbot;
