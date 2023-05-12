import React, { useState, useEffect } from 'react';
import axios from 'axios';
import USCardItem from './USCardItem';
import { Pagination, Button } from '@mui/material';
import { Box, Grid } from '@mui/material';

function AllProductsPage() {
  const [cards, setCards] = useState([]);
  const [sortedCards, setSortedCards] = useState([]);
  const [displaySorted, setDisplaySorted] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(20);

  useEffect(() => {
    const fetchAllCards = async () => {
      const response = await axios.get(`http://localhost:5000/api/all_us_prices`);
      const rate = sessionStorage.getItem('rate'); 

      const processedCards = response.data.map(card => {
        const JP_Price_USD = card.JP_price * rate;
        const priceDifference = card.US_price - JP_Price_USD;
        const priceDifferencePercentage = (priceDifference / card.US_price) * 100;
        return { ...card, JP_Price_USD, priceDifference, priceDifferencePercentage };
      });

      const sorted = [...processedCards].sort((a, b) => b.priceDifferencePercentage - a.priceDifferencePercentage);

      setCards(processedCards);
      setSortedCards(sorted);
    };

    fetchAllCards();
  }, []);

  const maxPage = Math.ceil((displaySorted ? sortedCards : cards).length / pageSize);

  const startIndex = (currentPage - 1) * pageSize;
  const endIndex = startIndex + pageSize;

  const currentPageCards = (displaySorted ? sortedCards : cards).slice(startIndex, endIndex);

  return (
    <div>
      <Box display="flex" alignItems="center"  mb={2}>
        <h1>All Pokémon Cards with Valid US Prices</h1>
        <Button variant="contained" color="primary" size="large" onClick={() => setDisplaySorted(!displaySorted)}>
          {displaySorted ? 'Display Normally' : 'Sort by Price Difference'}
        </Button>
      </Box>
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


