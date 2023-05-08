import React, { useState } from 'react';

const ExchangeRatePage = () => {
  const [baseCurrency, setBaseCurrency] = useState('USD');
  const [targetCurrency, setTargetCurrency] = useState('JPY');
  const [baseCurrencyAmount, setBaseCurrencyAmount] = useState('');
  const [targetCurrencyAmount, setTargetCurrencyAmount] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchExchangeRate = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5000/api/get_exchange_rate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ baseCurrency, targetCurrency }),
      });

      const data = await response.json();
      console.log(data);
      const exchangeRate = data.rate;
      const newTargetCurrencyAmount = baseCurrencyAmount * exchangeRate;
      setTargetCurrencyAmount(newTargetCurrencyAmount);
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
    <div>
      <h1>Exchange Rate Page</h1>
      <label>
        Base Currency:
        <select value={baseCurrency} onChange={(e) => setBaseCurrency(e.target.value)}>
          <option value="USD">USD</option>
          <option value="JPY">JPY</option>
        </select>
      </label>
      <label>
        Target Currency:
        <select value={targetCurrency} onChange={(e) => setTargetCurrency(e.target.value)}>
          <option value="USD">USD</option>
          <option value="JPY">JPY</option>
        </select>
      </label>
      <br />
      <label>
        Base Currency Amount:
        <input type="number" value={baseCurrencyAmount} onChange={handleInputChange} />
      </label>
      <button onClick={handleButtonClick}>Convert</button>
      {loading && <p>Loading...</p>}
      <p>Target Currency Amount: {targetCurrencyAmount}</p>
    </div>
  );
};

export default ExchangeRatePage;
