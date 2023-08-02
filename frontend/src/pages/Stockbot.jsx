const Stockbot = () => {
   return (
     <div className="flex flex-col items-center justify-center h-screen">
      <div className="fixed bottom-4 bg-gray-400 p-6 rounded-lg w-5/6">
      <input
           type="text"
           className="w-full bg-white border border-gray-400 rounded px-4 py-2 mt-2"
           placeholder="Type here..."
         />
      </div>
      <div className="fixed top-24 bg-gray-400 p-6 rounded-lg w-5/6">
      <div className="bg-gray-400 p-6 rounded-lg w-5/6 h-80 mt-4">
         <h3></h3>
       </div>
      </div>
     </div>
   );
 };
 
 export default Stockbot;
 
 