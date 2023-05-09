import React from 'react';
import { Card, CardContent, Typography, CardMedia } from '@mui/material';

const USCardItem = ({ card }) => {
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
      </CardContent>
    </Card>
  );
};

export default USCardItem;
