import React,{ useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import MainPage from './components/MainPage';
import SearchPage from './components/SearchPage';
import AllProductsPage from './components/AllProductsPage';
import ShippingPage from './components/ShippingPage';
import ExchangeRatePage from './components/ExchangeRate';
import Navbar from './components/Navbar';
import IconButton from '@mui/material/IconButton';
import PaidIcon from '@mui/icons-material/Paid';
import Drawer from '@mui/material/Drawer';

function App() {
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [exchangeRate, setExchangeRate] = useState(null);

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen);
  };

  useEffect(() => {
    fetch('http://localhost:5000/api/get_exchange_rate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        baseCurrency: 'JPY',
        targetCurrency: 'USD'
      })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      sessionStorage.setItem('rate', data.rate);
      setExchangeRate(data.rate);
    })
    .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
    });
  }, []); // Empty dependency array means this effect runs once when the component mounts.

  return (
    <Router>
      <div>
        <Navbar />

        <Routes>
          <Route path="/" element={<AllProductsPage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/volatile_card" element={<MainPage />} />
          <Route path="/shipping" element={<ShippingPage />} />
          <Route path="/get_exchange_rate" element={<ExchangeRatePage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
