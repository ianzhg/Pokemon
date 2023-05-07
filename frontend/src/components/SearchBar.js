import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';

const SearchBar = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    onSearch(searchTerm);
  };

  return (
    <Box component="form" onSubmit={handleSearch} display="flex">
      <TextField
        label="Search Pokémon Cards"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <Button type="submit" variant="contained" color="primary">
        Search
      </Button>
    </Box>
  );
};

export default SearchBar;
