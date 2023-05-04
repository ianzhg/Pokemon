import React, { useState } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

const data = Array.from({ length: 50 }, (_, i) => `Item ${i + 1}`);

const App = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(10);

  const handleClick = (event) => {
    setCurrentPage(Number(event.target.id));
  };

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = data.slice(indexOfFirstItem, indexOfLastItem);

  const renderItems = currentItems.map((item, index) => {
    return <li key={index}>{item}</li>;
  });

  const pageNumbers = [];
  for (let i = 1; i <= Math.ceil(data.length / itemsPerPage); i++) {
    pageNumbers.push(i);
  }

  const renderPageNumbers = pageNumbers.map((number) => {
    return (
      <li
        key={number}
        id={number}
        onClick={handleClick}
        className={currentPage === number ? "active" : ""}
      >
        {number}
      </li>
    );
  });

  return (
    <div className="App">
      <h1>Pagination Example</h1>
      <ul>{renderItems}</ul>
      <ul id="page-numbers" className="pagination">
        {renderPageNumbers}
      </ul>
    </div>
  );
};

export default App;