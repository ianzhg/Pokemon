import React, { useState } from 'react';
import CardItem from './CardItem';

function SearchPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchSubmit = async (event) => {
    event.preventDefault();
    // Replace 'https://your-api-endpoint.com/search' with your actual API endpoint for searching cards
    const response = await fetch(`https://your-api-endpoint.com/search?term=${searchTerm}`);
    const data = await response.json();
    setSearchResults(data);
  };

  return (
    <div>
      <h1>Search Cards</h1>
      <form onSubmit={handleSearchSubmit}>
        <input
          type="text"
          placeholder="Search..."
          value={searchTerm}
          onChange={handleSearchChange}
        />
        <button type="submit">Search</button>
      </form>
      <div>
        {searchResults.map((card) => (
          <CardItem key={card.name} card={card} />
        ))}
      </div>
    </div>
  );
}

export default SearchPage;
