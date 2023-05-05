// src/RunAllForm.js
import React, { useState } from "react";
import axios from "axios";

const RunAllForm = () => {
  const [cards, setCards] = useState("");
  const [jpZipcode, setJpZipcode] = useState("");
  const [usZipcode, setUsZipcode] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/runall", {
        cards,
        jp_zipcode: jpZipcode,
        us_zipcode: usZipcode,
      });
      console.log("Data received:", response.data);
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
        <button type="submit">Run</button>
      </form>
      {result && (
        <div>
          <h3>Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default RunAllForm;
