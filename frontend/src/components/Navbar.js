import React, { useState } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
  Drawer,
} from '@mui/material';
import { Link } from 'react-router-dom';
import PaidIcon from '@mui/icons-material/Paid';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import ExchangeRate from './ExchangeRate';
import Cart from './Cart';

const Navbar = () => {
  const [exchangeDrawerOpen, setExchangeDrawerOpen] = useState(false);
  const [cartDrawerOpen, setCartDrawerOpen] = useState(false);

  const toggleExchangeDrawer = () => {
    setExchangeDrawerOpen(!exchangeDrawerOpen);
  };

  const toggleCartDrawer = () => {
    setCartDrawerOpen(!cartDrawerOpen);
  };

  return (
    <>
      <AppBar position="static" sx={{ backgroundColor: '#1976d2' }}>
        <Toolbar sx={{ display: 'flex', justifyContent: 'space-between' }}>
          <Typography
            variant="h6"
            component={Link}
            to="/"
            sx={{ flexGrow: 1, textDecoration: 'none', color: 'white' }}
          >
            Pokémon Cards
          </Typography>
          <Box
            sx={{
              display: 'flex',
              justifyContent: 'flex-end',
              alignItems: 'center',
            }}
          >
            <Button
              color="inherit"
              component={Link}
              to="/search"
              sx={{ mr: 2 }}
            >
              Search
            </Button>
            <Button
              color="inherit"
              component={Link}
              to="/volatile_card"
              sx={{ mr: 2 }}
            >
              Volatile Cards
            </Button>
            <Button
              color="inherit"
              component={Link}
              to="/shipping"
              sx={{ mr: 2 }}
            >
              Shipping
            </Button>
            <Button
              color="inherit"
              component={Link}
              to="/get_exchange_rate"
              sx={{ mr: 2 }}
            >
              Currency Exchange
            </Button>
            <IconButton onClick={toggleExchangeDrawer}>
              <PaidIcon fontSize="large" />
            </IconButton>
            <IconButton onClick={toggleCartDrawer} sx={{ ml: 2 }}>
              <ShoppingCartIcon fontSize="large" />
            </IconButton>
          </Box>
        </Toolbar>
      </AppBar>
      <Drawer
        anchor="right"
        open={exchangeDrawerOpen}
        onClose={toggleExchangeDrawer}
      >
        <ExchangeRate />
      </Drawer>
      <Drawer anchor="right" open={cartDrawerOpen} onClose={toggleCartDrawer}>
        <Cart />
      </Drawer>
    </>
  );
};

export default Navbar;

