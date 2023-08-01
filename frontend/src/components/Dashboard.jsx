// src/components/Dashboard.js
import React from 'react';

const Dashboard = () => {
  return (
    <div className="container mx-auto mt-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div className="bg-gray-400 p-6 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-xl font-bold mb-2">Stocks and Futures</h3>
          <p className="text-gray-700">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div className="bg-gray-400 p-6 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-xl font-bold mb-2">Forex</h3>
          <p className="text-gray-700">Sed id leo vel felis fermentum dignissim.</p>
        </div>
        <div className="bg-gray-400 p-6 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-xl font-bold mb-2">Indices and Bonds</h3>
          <p className="text-gray-700">Nulla porttitor fringilla blandit. Vivamus id aliquam turpis.</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
