import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainPage from './components/MainPage';
import SearchPage from './components/SearchPage';
import AllProductsPage from './components/AllProductsPage';
import ShippingPage from './components/ShippingPage';
import ExchangeRatePage from './components/ExchangeRate';
import Navbar from './components/Navbar'; // import the Navbar component

function App() {
  return (
    <Router>
      <div>
        <Navbar /> {/* replace the raw nav element with the Navbar component */}
        
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/all-products" element={<AllProductsPage />} />
          <Route path="/shipping" element={<ShippingPage />} />
          <Route path="/get_exchange_rate" element={<ExchangeRatePage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;



