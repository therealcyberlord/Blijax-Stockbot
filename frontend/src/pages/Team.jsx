const Team = () => {
  return (
    <div className="container mx-auto mt-8">
      <div className="flex justify-center">
        <div className="flex flex-col items-center">
          <div className="bg-blue-400 p-6 rounded-full shadow-lg shadow-blue-600 transform transition-all hover:scale-105 mb-4">
            <img
              src="https://media.licdn.com/dms/image/D5603AQFl7NojGBGsyQ/profile-displayphoto-shrink_200_200/0/1683256979553?e=1697068800&v=beta&t=SxycuDnX7eQfgdNB7lfmdvKD95mlCiTC9LOxGcvWo2o"
              alt="Image 1"
              className="w-full rounded-full"
            />
          </div>
          <h3 className="text-xl font-bold mb-2">Blake Almon - Backend</h3>
        </div>
        <div className="flex flex-col items-center">
          <div className="bg-blue-400 p-6 rounded-full shadow-lg shadow-blue-600 transform transition-all hover:scale-105 mb-4">
            <img
              src="/src/assets/aaron.png"
              alt="Image 2"
              className="w-full rounded-full"
            />
          </div>
          <h3 className="text-xl font-bold mb-2">Aaron Nguy - Backend</h3>
        </div>
        <div className="flex flex-col items-center">
          <div className="bg-blue-400 p-6 rounded-full shadow-lg shadow-blue-600 transform transition-all hover:scale-105 mb-4">
            <img
              src="/src/assets/sophia.png"
              alt="Image 3"
              className="w-full rounded-full"
            />
          </div>
          <h3 className="text-xl font-bold mb-2">Sophia Lee - Frontend</h3>
        </div>
        <div className="flex flex-col items-center">
          <div className="bg-blue-400 p-6 rounded-full shadow-lg shadow-blue-600 transform transition-all hover:scale-105 mb-4">
            <img
              src="/src/assets/isaac.png"
              alt="Image 4"
              className="w-full rounded-full"
            />
          </div>
          <h3 className="text-xl font-bold mb-2">Isaac Jung - Backend</h3>
        </div>
        <div className="flex flex-col items-center">
          <div className="bg-blue-400 p-6 rounded-full shadow-lg shadow-blue-600 transform transition-all hover:scale-105 mb-4">
            <img
              src="/src/assets/jackson.png"
              alt="Image 5"
              className="w-full rounded-full"
            />
          </div>
          <h3 className="text-xl font-bold mb-2">Jackson Pirooz - Frontend</h3>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="flex flex-col items-center">
          <div className="bg-blue-400 p-8 rounded-full shadow-lg shadow-blue-600 transform transition-all hover:scale-105 mb-4">
            <img
              src="https://media.licdn.com/dms/image/D4E03AQFCQkdaurjz6w/profile-displayphoto-shrink_200_200/0/1683933220891?e=1697068800&v=beta&t=aVluXLWW0I837MolLBSxxTUp9noW3EB_gVmnlZ0pQCM"
              alt="Image 6"
              className="w-full rounded-full"
            />
          </div>
          <h3 className="text-xl font-bold mb-2">
            Xingyu Bian - Product Manager
          </h3>
        </div>
      </div>
    </div>
  );
};

export default Team;
