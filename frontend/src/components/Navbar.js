import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <AppBar position="static" sx={{ backgroundColor: '#1976d2' }}>
      <Toolbar sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography variant="h6" component={Link} to="/" sx={{ flexGrow: 1, textDecoration: 'none', color: 'white' }}>
          Pokémon Cards
        </Typography>
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'center' }}>
          <Button color="inherit" component={Link} to="/search" sx={{ mr: 2 }}>
            Search
          </Button>
          <Button color="inherit" component={Link} to="/all">
            All Products
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
