import React, { useState, useEffect} from 'react';
import {
  Container,
  Grid,
  Typography,
  Select,
  MenuItem,
  TextField,
  Button,
  CircularProgress,
} from '@mui/material';


const ExchangeRatePage = () => {
  const [baseCurrency, setBaseCurrency] = useState('USD');
  const [targetCurrency, setTargetCurrency] = useState('JPY');
  const [baseCurrencyAmount, setBaseCurrencyAmount] = useState('');
  const [targetCurrencyAmount, setTargetCurrencyAmount] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const storedTargetCurrencyAmount = sessionStorage.getItem('targetCurrencyAmount');
    if (storedTargetCurrencyAmount) {
      setTargetCurrencyAmount(storedTargetCurrencyAmount);
    }
  }, []);

  const fetchExchangeRate = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5000/api/get_exchange_rate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ baseCurrency, targetCurrency }),
      });

      const data = await response.json();
      const exchangeRate = data.rate;
      const newTargetCurrencyAmount = baseCurrencyAmount * exchangeRate;
      setTargetCurrencyAmount(newTargetCurrencyAmount);
      setTargetCurrencyAmount(newTargetCurrencyAmount);
      sessionStorage.setItem('targetCurrencyAmount', newTargetCurrencyAmount);
    } catch (error) {
      console.error('Error fetching exchange rate:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    setBaseCurrencyAmount(e.target.value);
  };

  const handleButtonClick = () => {
    fetchExchangeRate();
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        Currency Exchange
      </Typography>
      <Grid container spacing={2} alignItems="center" justifyContent="center">
        <Grid item xs={12} md={6}>
          <Typography variant="subtitle1">Base Currency:</Typography>
          <Select
            value={baseCurrency}
            onChange={(e) => setBaseCurrency(e.target.value)}
            fullWidth
          >
            <MenuItem value="USD">USD</MenuItem>
            <MenuItem value="JPY">JPY</MenuItem>
          </Select>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography variant="subtitle1">Target Currency:</Typography>
          <Select
            value={targetCurrency}
            onChange={(e) => setTargetCurrency(e.target.value)}
            fullWidth
          >
            <MenuItem value="USD">USD</MenuItem>
            <MenuItem value="JPY">JPY</MenuItem>
          </Select>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography variant="subtitle1">Base Currency Amount:</Typography>
          <TextField
            type="number"
            value={baseCurrencyAmount}
            onChange={handleInputChange}
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <Button variant="contained" color="primary" onClick={handleButtonClick} fullWidth>
            Convert
          </Button>
        </Grid>
        <Grid item xs={12}>
          {loading ? (
            <CircularProgress />
          ) : (
            <Typography variant="h6">Target Currency Amount: {targetCurrencyAmount}</Typography>
          )}
        </Grid>
      </Grid>
    </Container>
  );
};

export default ExchangeRatePage;
