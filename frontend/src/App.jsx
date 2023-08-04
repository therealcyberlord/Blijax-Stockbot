// src/App.js
import {Route, Switch} from 'wouter';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import About from './pages/About';
import Stockbot from './pages/Stockbot';
import './App.css';

function App() {
  return (
    <div className="bg-white">
      <Navbar />
         <Switch>
          <Route path='/' component={Dashboard} />
          <Route path='/about' component={About} />
          <Route path='/stockbot' component={Stockbot} />
         </Switch>
    </div>
  );
}

export default App;


