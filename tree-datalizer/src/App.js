import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/home';
import Analytics from './pages/analytics';
import Navbar from './components/navbar';
function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path = '/' element={<Home/>} />
        <Route path = '/analytics' element={<Analytics/>} />
      </Routes>
    </Router>
  );
}

export default App;
