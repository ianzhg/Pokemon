import React, { useState } from 'react';
import '../css/ShippingPage.css';
import japanPostImage from '../image/Japan-post.jpg';
import DHLImage from '../image/DHL_logo.png';
import FedexImage from '../image/FedEx_logo.jpg';

const ShippingPage = () => {
    const [cards, setCards] = useState('');
    const [usZip, setUsZip] = useState('');
    const [japanZip, setJapanZip] = useState('');
    const [JapanPostresult, setJapanResult] = useState('');
    const [DHLresult, setDHLResult] = useState('');
    const [Fedexresult, setFedexResult] = useState('');
    const [loading, setLoading] = useState(false);
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      setLoading(true); // Start loading

      // try{
      //   const response = await fetch('http://localhost:5000/api/shipping_japan_post', {
      //       method: 'POST',
      //       headers: { 'Content-Type': 'application/json' },
      //       body: JSON.stringify({ cards, usZip, japanZip }),
      //     });
        
      //     const data = await response.json();
      //     setJapanResult(data);
      // } catch (error){
      //   console.error("Error fetching data:",  error);
      // }finally{
      //   setLoading(false);
      // }

      // try{
      //   const response = await fetch('http://localhost:5000/api/shipping_DHL', {
      //       method: 'POST',
      //       headers: { 'Content-Type': 'application/json' },
      //       body: JSON.stringify({ cards, usZip, japanZip }),
      //     });
        
      //     const data = await response.json();
      //     setDHLResult(data);
      // } catch (error){
      //   console.error("Error fetching data:",  error);
      // }finally{
      //   setLoading(false);
      // }


      try{
        const response = await fetch('http://localhost:5000/api/shipping_Fedex', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cards, usZip, japanZip }),
          });
        
          const data = await response.json();
          setFedexResult(data);
      } catch (error){
        console.error("Error fetching data:",  error);
      }finally{
        setLoading(false);
      }


    };


    const renderJapanResult = () => {
      if (!JapanPostresult) return null;
  
      return (
        <div>
          <h3>Shipping Info</h3>
          <pre>{JapanPostresult.shipping_info}</pre>
          <p><b>Fastest Way:</b> {JapanPostresult.fastest_way} {JapanPostresult.fastest_way_cost_and_time}  <a href={JapanPostresult.fatstest_link} target="_blank" rel="noopener noreferrer">Click Here</a></p>
          <p><b>Other Shipping Methods</b></p>
          <ul>
            {Object.entries(JapanPostresult)
              .filter(([key]) => key !== 'shipping_info' && key !== 'fastest_way' && key !== 'fastest_way_cost_and_time' && key !== 'fatstest_link')
              .map(([key, value]) => (
                <li key={key}>
                  <strong>{key}:</strong>
                  <pre>{value}</pre>
                </li>
              ))}
          </ul>
        </div>
      );
    };

    const renderDHLResult = () => {
      if (!DHLresult) return null;
  
      return (
        <div>
          <h3>Shipping Info</h3>
          <ul>
            {Object.entries(DHLresult)
              .filter(([key]) => key !== 'shipping_info' && key !== 'fastest_way' && key !== 'fastest_way_cost_and_time' && key !== 'fatstest_link')
              .map(([key, value]) => (
                <li key={key}>
                  <strong>{key}:</strong>
                  <pre>{value}</pre>
                </li>
              ))}
          </ul>
        </div>
      );
    };

    const renderFedexResult = () => {
      if (!Fedexresult) return null;
  
      return (
        <div>
          <h3>Shipping Info</h3>
          <ul>
            {Object.entries(Fedexresult)
              .filter(([key]) => key !== 'shipping_info' && key !== 'fastest_way' && key !== 'fastest_way_cost_and_time' && key !== 'fatstest_link')
              .map(([key, value]) => (
                <li key={key}>
                  <strong>{key}:</strong>
                  <pre>{value}</pre>
                </li>
              ))}
          </ul>
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
          {/* <div className={"container"}>
            <div className={"imageContainer"}>
              <img src={japanPostImage} alt="Japan Post" className={"img"}/>
            </div>
            {loading && <p>Loading...</p>}
            <div className={"content"}>{renderJapanResult()}</div>
          </div>

          <div className={"container"}>
            <div className={"imageContainer"}>
              <img src={DHLImage} alt="DHL" className={"img"}/>
            </div>
            {loading && <p>Loading...</p>}
            <div className={"content"}>{renderDHLResult()}</div>
          </div>   */}

          <div className={"container"}>
            <div className={"imageContainer"}>
              <img src={FedexImage} alt="Fedex" className={"img"}/>
            </div>
            {loading && <p>Loading...</p>}
            <div className={"content"}>{renderFedexResult()}</div>
          </div>  


        </div>
      );
    };
    
    export default ShippingPage;