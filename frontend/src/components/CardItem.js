import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const CardItem = ({ card }) => {
  return (
    <Card>
      <CardContent>
        <Typography variant="h5" component="div">
          {card.name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Collector Info: {card.collector_info}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Set: {card.set}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Rarity: {card.rarity}
        </Typography>
        <Typography variant="body1" color="text.primary">
          Price: {card.price}
        </Typography>
        <Typography variant="body1" color="text.primary">
          Shift: {card.shift}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default CardItem;
