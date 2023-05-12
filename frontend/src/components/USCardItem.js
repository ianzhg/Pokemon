import React from 'react';
import { Card, CardContent, Typography, CardMedia, Button } from '@mui/material';

const USCardItem = ({ card }) => {
  const addToCart = () => {
    let cart = JSON.parse(sessionStorage.getItem('cart')) || [];
    cart.push(card);
    sessionStorage.setItem('cart', JSON.stringify(cart));
  };

  // Fetch the rate from sessionStorage and parse it to float
  const rate = parseFloat(sessionStorage.getItem('rate'));
  
  // Calculate JP_Price_USD, priceDifference and percentageDifference
  const JP_Price_USD = card.JP_price * rate;
  const priceDifference = card.US_price - JP_Price_USD;
  const percentageDifference = (priceDifference / card.US_price) * 100;

  return (
    <Card>
      <CardMedia
        component="img"
        height="300"
        width="auto"
        image={card['Image URL']}
        alt={card.US_name}
      />
      <CardContent>
        <Typography variant="h5" component="div">
          {card.US_name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          US Price: {card.US_price.toFixed(2)}$
        </Typography>
        <Typography variant="body2" color="text.secondary">
          JP Price: {card.JP_price.toFixed(2)}¥
        </Typography>
        <Typography variant="body2" color="text.secondary">
          JP Price (USD): {JP_Price_USD.toFixed(2)}$
        </Typography>
        <Typography variant="body2" color={priceDifference > 0 ? "error" : "text.secondary"}>
          Price Difference: {priceDifference.toFixed(2)}$
        </Typography>
        <Typography variant="body2" color={priceDifference > 0 ? "error" : "text.secondary"}>
          Difference in Percentage: {percentageDifference.toFixed(2)}%
        </Typography>
        <Typography variant="body2" color="text.secondary">
          JP Name: {card.JP_name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Card ID: {card._id}
        </Typography>
        <Button variant="contained" color="primary" onClick={addToCart}>
          Add to Cart
        </Button>
      </CardContent>
    </Card>
  );
};

export default USCardItem;


