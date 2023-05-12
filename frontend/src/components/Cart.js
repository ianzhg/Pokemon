import React, { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Divider,
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);
  const rate = parseFloat(sessionStorage.getItem('rate')) || 0;

  useEffect(() => {
    const storedCart = JSON.parse(sessionStorage.getItem('cart')) || [];
    setCartItems(storedCart);
  }, []);

  const removeItemFromCart = (index) => {
    const updatedCartItems = [...cartItems];
    updatedCartItems.splice(index, 1);
    setCartItems(updatedCartItems);
    sessionStorage.setItem('cart', JSON.stringify(updatedCartItems));
  };

  const totalUSPrice = cartItems.reduce(
    (total, item) => total + parseFloat(item.US_price),
    0
  );

  const totalJPPriceUSD = cartItems.reduce(
    (total, item) => total + parseFloat(item.JP_price) * rate,
    0
  );

  const totalRawDifference = totalUSPrice - totalJPPriceUSD;
  const totalPercentageDifference = (totalRawDifference / totalUSPrice) * 100;

  return (
    <Box sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper', minHeight: 300 }}>
      <Box mt={2} mb={2}>
        <Typography variant="h6" align="center">
          Cart
        </Typography>
      </Box>
      <Divider />
      {cartItems.length === 0 ? (
        <Box mt={4}>
          <Typography variant="body1" align="center">
            Your cart is empty.
          </Typography>
        </Box>
      ) : (
        <>
          <List>
            {cartItems.map((item, index) => (
              <React.Fragment key={item.unique_id}>
                <ListItem>
                  <ListItemText
                    primary={item.US_name}
                    secondary={`US Price: $${item.US_price}, JP Price: $${(item.JP_price * rate).toFixed(2)}`}
                  />
                  <ListItemSecondaryAction>
                    <IconButton
                      edge="end"
                      aria-label="delete"
                      onClick={() => removeItemFromCart(index)}
                    >
                      <DeleteIcon />
                    </IconButton>
                  </ListItemSecondaryAction>
                </ListItem>
                {index !== cartItems.length - 1 && <Divider />}
              </React.Fragment>
            ))}
          </List>
          <Divider />
          <Box my={2}>
            <Typography variant="subtitle1" align="center">
              Total US Price: ${totalUSPrice.toFixed(2)}
            </Typography>
            <Typography variant="subtitle1" align="center">
              Total JP Price in USD: ${totalJPPriceUSD.toFixed(2)}
            </Typography>
            <Typography variant="subtitle1" align="center" color="error">
              Total Raw Difference: ${totalRawDifference.toFixed(2)}
            </Typography>
            <Typography variant="subtitle1" align="center" color="error">
              Total Percentage Difference: {totalPercentageDifference.toFixed(2)}%
            </Typography>
          </Box>
        </>
      )}
    </Box>
  );
};

export default Cart;

