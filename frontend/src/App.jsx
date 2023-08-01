// src/App.js
import React from 'react';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';

function App() {
  return (
    <div className="bg-white">
      <Navbar />
      <Dashboard />
    </div>
  );
}

export default App;
