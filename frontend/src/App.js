import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import MainPage from './components/MainPage';
import SearchPage from './components/SearchPage';
import AllProductsPage from './components/AllProductsPage';
import ShippingPage from './components/ShippingPage';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Main Page</Link>
            </li>
            <li>
              <Link to="/search">Search</Link>
            </li>
            <li>
              <Link to="/all-products">All Products</Link>
            </li>
            <li>
              <Link to="/shipping">Shipping</Link>
            </li>
            <li>
              <Link to="/currency">Currency Exchange</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/all-products" element={<AllProductsPage />} />
          <Route path="/shipping" element={<ShippingPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;


