// src/App.js
import { Route, Switch } from "wouter";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import Team from "./pages/Team";
import Stockbot from "./pages/Stockbot";
import About from "./pages/About";
import "./App.css";

function App() {
  return (
    <div className="bg-white">
      <Navbar />
      <Switch>
        <Route path="/" component={Dashboard} />
        <Route path="/team" component={Team} />
        <Route path="/stockbot" component={Stockbot} />
        <Route path="/about" component={About} />
      </Switch>
    </div>
  );
}

export default App;
