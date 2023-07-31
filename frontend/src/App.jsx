import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="bg-green-100 text-green-800">
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Stock Dashboard</h1>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
         
          <div className="bg-white rounded-lg p-4 shadow-md">
          
            <h2 className="text-lg font-semibold mb-2">Stock Index 1</h2>
            <p className="text-gray-600">Current Value: $100</p>
            <p className="text-gray-600">Change: +$5 (5%)</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-md">
        
            <h2 className="text-lg font-semibold mb-2">Stock Index 2</h2>
            <p className="text-gray-600">Current Value: $200</p>
            <p className="text-gray-600">Change: -$10 (-5%)</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-md">
            
            <h2 className="text-lg font-semibold mb-2">Stock Index 3</h2>
            <p className="text-gray-600">Current Value: $300</p>
            <p className="text-gray-600">Change: +$20 (7%)</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow-md">
            
            <h2 className="text-lg font-semibold mb-2">Stock Index 4</h2>
            <p className="text-gray-600">Current Value: $400</p>
            <p className="text-gray-600">Change: +$15 (3.5%)</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
