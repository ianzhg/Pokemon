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
          setResult(data.result);
      } catch (error){
        console.error("Error fetching data:",  error);
      }finally{
        setLoading(false);
      }

  
      
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
          {result && <p>Result: {result}</p>}
        </div>
      );
    };
    
    export default ShippingPage;