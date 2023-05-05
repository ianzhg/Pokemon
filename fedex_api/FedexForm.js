// src/FedexForm.js
import React, { useState } from "react";
import axios from "axios";

const FedexForm = () => {
  const [cards, setCards] = useState("");
  const [jpZipcode, setJpZipcode] = useState("120-0011");
  const [usZipcode, setUsZipcode] = useState("90001");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/fedex", {
        cards,
        jp_zipcode: jpZipcode,
        us_zipcode: usZipcode,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Cards:
          <input
            type="number"
            value={cards}
            onChange={(e) => setCards(e.target.value)}
          />
        </label>
        <label>
          JP Zipcode:
          <input
            type="text"
            value={jpZipcode}
            onChange={(e) => setJpZipcode(e.target.value)}
          />
        </label>
        <label>
          US Zipcode:
          <input
            type="text"
            value={usZipcode}
            onChange={(e) => setUsZipcode(e.target.value)}
          />
        </label>
        <button type="submit">Get Shipping Info</button>
      </form>
      {result && (
        <div>
          <h3>Shipping Information</h3>
          <p>Shipment Date: {result.shipment_date}</p>
          <h4>Arrival Times and Prices:</h4>
          <ul>
            {Object.entries(result.arrive_and_price).map(([key, value]) => (
              <li key={key}>
                {key}: {value}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default FedexForm;
