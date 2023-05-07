import React, { useState, useEffect } from 'react';
import CardItem from './CardItem';

function AllProductsPage() {
  const [cards, setCards] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    const fetchAllCards = async () => {
      // Replace 'https://your-api-endpoint.com/all_cards' with your actual API endpoint for fetching all cards
      const response = await fetch(`https://your-api-endpoint.com/all_cards?page=${currentPage}`);
      const data = await response.json();
      setCards(data);
    };

    fetchAllCards();
  }, [currentPage]);

  const handlePrevPage = () => {
    setCurrentPage((prevPage) => Math.max(prevPage - 1, 1));
  };

  const handleNextPage = () => {
    setCurrentPage((prevPage) => prevPage + 1);
  };

  return (
    <div>
      <h1>All Pokémon Cards</h1>
      <div>
        {cards.map((card) => (
          <CardItem key={card.name} card={card} />
        ))}
      </div>
      <button onClick={handlePrevPage}>Prev</button>
      <button onClick={handleNextPage}>Next</button>
    </div>
  );
}

export default AllProductsPage;
