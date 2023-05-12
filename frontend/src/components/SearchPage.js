import React, { useState, useEffect } from 'react';
import axios from 'axios';
import USCardItem from './USCardItem';
import { Pagination } from '@mui/material';
import { Box, Grid, TextField, Button } from '@mui/material';

function SearchPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(20);

  useEffect(() => {
    const fetchSearchResults = async () => {
      if (searchTerm) {
        const response = await axios.get(`http://localhost:5000/api/search?term=${searchTerm}`);
        setSearchResults(response.data);
        console.log(response.data);
      } else {
        setSearchResults([]);
      }
    };

    fetchSearchResults();
  }, [searchTerm]);

  const maxPage = Math.ceil(searchResults.length / pageSize);

  const startIndex = (currentPage - 1) * pageSize;
  const endIndex = startIndex + pageSize;

  const currentPageResults = searchResults.slice(startIndex, endIndex);

  return (
    <div>
      <h1>Search Pokémon Cards</h1>
      <Box mb={4}>
        <form onSubmit={(e) => e.preventDefault()}>
          <TextField
            label="Search Pokémon Cards"
            variant="outlined"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <Button type="submit" variant="contained" color="primary">
            Search
          </Button>
        </form>
      </Box>
      <Grid container spacing={2}>
        {currentPageResults.map((card) => (
          <Grid item xs={12} sm={6} md={4} key={card._id}>
            <USCardItem card={card} />
          </Grid>
        ))}
      </Grid>
      <Box my={4}>
        <Pagination
          count={maxPage}
          page={currentPage}
          onChange={(event, value) => setCurrentPage(value)}
        />
      </Box>
    </div>
  );
}

export default SearchPage;
