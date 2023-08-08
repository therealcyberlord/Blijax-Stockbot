const Box = ({ imageUrl, altText, text }) => {
  return (
    <div className="bg-gray-400 p-6 rounded-lg shadow-lg shadow-emerald-500 transform transition-all hover:scale-105">
      <img src={imageUrl} alt={altText} className="w-full mb-4" />
      <h3 className="text-xl font-bold mb-2">{text}</h3>
    </div>
  );
};

export default Box;
