const ImageBox = ({ name, role, img }) => {
  return (
    <div className="flex flex-col items-center w-full sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/5 p-4">
      <div className="bg-blue-400 p-6 rounded-full shadow-lg shadow-blue-600 transform transition-all hover:scale-105 mb-4">
        <img
          src={img}
          alt={`Team Member ${name}`}
          className="w-full rounded-full"
        />
      </div>
      <h3 className="text-xl font-bold mb-2">{name}</h3>
      <p>{role}</p>
    </div>
  );
};

export default ImageBox;
