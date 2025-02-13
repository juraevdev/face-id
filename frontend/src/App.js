import React from 'react';
import { BrowserRouter as Router, Route, BrowserRouter, Routes } from 'react-router-dom';
import Login from './components/Login';   

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='login/' element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
