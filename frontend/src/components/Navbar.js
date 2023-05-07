import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component={Link} to="/" style={{ flexGrow: 1, textDecoration: 'none', color: 'inherit' }}>
          Pokémon Cards
        </Typography>
        <Button color="inherit" component={Link} to="/search">
          Search
        </Button>
        <Button color="inherit" component={Link} to="/all">
          All Products
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
