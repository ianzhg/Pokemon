import React from 'react';
import { Card, CardContent, Typography, CardMedia, Button } from '@mui/material';

const USCardItem = ({ card }) => {
  const addToCart = () => {
    let cart = JSON.parse(sessionStorage.getItem('cart')) || [];
    cart.push(card);
    sessionStorage.setItem('cart', JSON.stringify(cart));
  };

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
          US Price: {card.US_price}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          JP Price: {card.JP_price}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          JP Name: {card.JP_name}
        </Typography>
        <Typography variant="body2" color="text.primary">
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

