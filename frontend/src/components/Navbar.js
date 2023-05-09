import React, { useState } from 'react';
import { AppBar, Toolbar, Typography, Button, Box, IconButton, Drawer } from '@mui/material';
import { Link } from 'react-router-dom';
import PaidIcon from '@mui/icons-material/Paid';
import ExchangeRate from './ExchangeRate';

const Navbar = () => {
  const [drawerOpen, setDrawerOpen] = useState(false);

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen);
  };

  return (
    <>
      <AppBar position="static" sx={{ backgroundColor: '#1976d2' }}>
        <Toolbar sx={{ display: 'flex', justifyContent: 'space-between' }}>
          <Typography variant="h6" component={Link} to="/" sx={{ flexGrow: 1, textDecoration: 'none', color: 'white' }}>
            Pokémon Cards
          </Typography>
          <Box sx={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'center' }}>
            <Button color="inherit" component={Link} to="/search" sx={{ mr: 2 }}>
              Search
            </Button>
            <Button color="inherit" component={Link} to="/all-products" sx={{ mr: 2 }}>
              All Products
            </Button>
            <Button color="inherit" component={Link} to="/shipping" sx={{ mr: 2 }}>
              Shipping
            </Button>
            <Button color="inherit" component={Link} to="/get_exchange_rate" sx={{ mr: 2 }}>
              Currency Exchange
            </Button>
            <IconButton onClick={toggleDrawer}>
              <PaidIcon fontSize="large" />
            </IconButton>
          </Box>
        </Toolbar>
      </AppBar>
      <Drawer anchor="right" open={drawerOpen} onClose={toggleDrawer}>
        <ExchangeRate />
      </Drawer>
    </>
  );
};

export default Navbar;

