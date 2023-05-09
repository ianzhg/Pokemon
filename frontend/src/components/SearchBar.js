import React, { useState, useEffect } from 'react';
import { TextField, Box } from '@mui/material';

const SearchBar = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    const timer = setTimeout(() => {
      onSearch(searchTerm);
    }, 500);

    return () => {
      clearTimeout(timer);
    };
  }, [searchTerm, onSearch]);

  return (
    <Box
      component="form"
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
    </Box>
  );
};

export default SearchBar;


