import React,{ useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import MainPage from './components/MainPage';
import SearchPage from './components/SearchPage';
import AllProductsPage from './components/AllProductsPage';
import ShippingPage from './components/ShippingPage';
import ExchangeRatePage from './components/ExchangeRate';
import Navbar from './components/Navbar'; // import the Navbar component
import IconButton from '@mui/material/IconButton';
import PaidIcon from '@mui/icons-material/Paid';
import Drawer from '@mui/material/Drawer';

function App() {
  const [drawerOpen, setDrawerOpen] = useState(false);

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen);
  };


  return (
    <Router>
      <div>
        <Navbar /> {/* replace the raw nav element with the Navbar component */}
        
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



