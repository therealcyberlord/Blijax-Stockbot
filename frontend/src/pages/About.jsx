const About = () => {
  return (
    <div className="bg-white-400 min-h-screen flex justify-center items-center">
      <div className="w-5/6 h-2/3 p-8 bg-gray-600 rounded-lg shadow-md flex">
        <img
          src="src/assets/stockbot.jpg"
          alt="Product"
          width="500"
          height="100"
        />
        <div className="flex flex-col justify-center ml-8">
          <h2 className="text-4xl font-semibold mb-4 text-gray-100">
            About Us
          </h2>
          <p className="text-3xl mb-4 text-gray-100">
            Our product will predict the trend of the stock market based on the
            news of the day (WSJ, economic news, press releases, laws passed,
            summarized SEC Filings, CPI reports, FOMC rates, and Company News).
            Based on the data our product will help customers understand the
            stock market better, allowing better financial decisions. In
            addition, our product provides advice on purchasing stocks using a
            virtual assistant that customers can chat with. Question Submission:
            Our interactive website provides a way to submit a question about
            the stock market into our model. Language Integration Model: After
            being able to submit a question the integrated language model in our
            site should be able to understand the language and provide a
            response in an adequate way. Response Generation: The site should be
            able to generate a response answering their question about the stock
            market in an accurate way. This response will be written in a clear
            and concise way.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;
