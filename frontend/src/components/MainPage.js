import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CardItem from './CardItem';

function MainPage() {
  const [volatileCards, setVolatileCards] = useState([]);

  useEffect(() => {
    axios
      .get('your_api_endpoint_here')
      .then((response) => {
        setVolatileCards(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Most Volatile Cards</h1>
      <div>
        {volatileCards && volatileCards.map((card) => (
          <CardItem key={card.id} card={card} />
        ))}
      </div>
    </div>
  );
}

export default MainPage;

