import React, { useState, useEffect } from 'react';
import axios from 'axios';
import USCardItem from './USCardItem';
import { Pagination } from '@mui/material';
import { Box, Grid } from '@mui/material';

function AllProductsPage() {
  const [cards, setCards] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(20);

  useEffect(() => {
    const fetchAllCards = async () => {
      const response = await axios.get(`http://localhost:5000/api/all_us_prices`);

      setCards(response.data);
    };

    fetchAllCards();
  }, []);

  const maxPage = Math.ceil(cards.length / pageSize);

  const startIndex = (currentPage - 1) * pageSize;
  const endIndex = startIndex + pageSize;

  const currentPageCards = cards.slice(startIndex, endIndex);

  return (
    <div>
      <h1>All Pokémon Cards with Valid US Prices</h1>
      <Grid container spacing={2}>
        {currentPageCards.map((card) => (
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

export default AllProductsPage;

