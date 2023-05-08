import React, { useState } from 'react';

const ShippingPage = () => {
    const [cards, setCards] = useState('');
    const [usZip, setUsZip] = useState('');
    const [japanZip, setJapanZip] = useState('');
    const [result, setResult] = useState('');
    const [loading, setLoading] = useState(false);
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      setLoading(true); // Start loading

      try{
        const response = await fetch('http://localhost:5000/api/shipping', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cards, usZip, japanZip }),
          });
        
          const data = await response.json();
          console.log(data)
          setResult(data);
      } catch (error){
        console.error("Error fetching data:",  error);
      }finally{
        setLoading(false);
      }
    };

    const renderResult = () => {
      if (!result) return null;
  
      return (
        <div>
          <h3>Shipping Info</h3>
          <pre>{result.shipping_info}</pre>
          <h3>Fastest Way</h3>
          <p>{result.fastest_way}</p>
          <p>{result.fastest_way_cost_and_time}</p>
          <p>
            <a href={result.fatstest_link} target="_blank" rel="noopener noreferrer">
              {result.fatstest_link}
            </a>
          </p>
          <h3>Other Shipping Methods</h3>
          {/* <ul>
            {Object.entries(result)
              .filter(([key]) => key !== 'shipping_info' && key !== 'fastest_way' && key !== 'fastest_way_cost_and_time' && key !== 'fatstest_link')
              .map(([key, value]) => (
                <li key={key}>
                  <strong>{key}:</strong>
                  <pre>{value}</pre>
                </li>
              ))}
          </ul> */}
        </div>
      );
    };

    return (
        <div>
          <h1>Shipping Page</h1>
          <form onSubmit={handleSubmit}>
            <label>
              Cards:
              <input value={cards} onChange={(e) => setCards(e.target.value)} />
            </label>
            <label>
              US Zip Code:
              <input value={usZip} onChange={(e) => setUsZip(e.target.value)} />
            </label>
            <label>
              Japan Zip Code:
              <input value={japanZip} onChange={(e) => setJapanZip(e.target.value)} />
            </label>
            <button type="submit">Submit</button>
          </form>
          {loading && <p>Loading...</p>}
          {renderResult()}
        </div>
      );
    };
    
    export default ShippingPage;