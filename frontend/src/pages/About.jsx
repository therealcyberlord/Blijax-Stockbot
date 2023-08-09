import React from "react";

const About = () => {
  return (
    <div className="bg-white-400 min-h-screen flex justify-center items-center">
      <div className="w-5/6 h-2/3 p-8 bg-blue-600 rounded-lg shadow-md flex flex-col md:flex-row items-center">
        <img
          src="src/assets/stockbot.jpg"
          alt="Product"
          className="w-1/4 md:w-1/6 h-auto rounded-lg mb-4 md:mb-0"
        />
        <div className="md:ml-8">
          <h2 className="text-4xl font-semibold mb-4 text-gray-100">
            About Us
          </h2>
          <p className="text-3xl mb-4 text-blue-100">
            Our product will predict the trend of the stock market based on the
            news of the day (WSJ, economic news, press releases, laws passed,
            summarized SEC Filings, CPI reports, FOMC rates, and Company News).
            Based on the data our product will help customers understand the
            stock market better, allowing better financial decisions. In
            addition, our product provides advice on purchasing stocks using a
            virtual assistant that customers can chat with.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;
