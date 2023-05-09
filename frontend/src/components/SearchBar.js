import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';

const SearchBar = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    onSearch(searchTerm);
  };

  return (
    <Box
      component="form"
      onSubmit={handleSearch}
      display="flex"
      alignItems="center"
      justifyContent="center"
      sx={{ height: '100%' }}
    >
      <Box sx={{ mr: 1 }}>
        <TextField
          label="Search Pokémon Cards"
          variant="outlined"
          size="small"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </Box>
      <Button type="submit" variant="contained" color="primary">
        Search
      </Button>
    </Box>
  );
};

export default SearchBar;

