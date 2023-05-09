import React, { useState } from 'react';
import '../css/ShippingPage.css';
import japanPostImage from '../image/Japan-post.jpg';
import DHLImage from '../image/dhl-logo.jpg';
import FedexImage from '../image/FedEx_logo.jpg';
import CircularProgress from '@mui/material/CircularProgress';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/system';

const ShippingPage = () => {
    const [cards, setCards] = useState('');
    const [usZip, setUsZip] = useState('');
    const [japanZip, setJapanZip] = useState('');

    const [JapanPostresult, setJapanResult] = useState(JSON.parse(sessionStorage.getItem('japanPostResult')) || '');
    const [DHLresult, setDHLResult] = useState(JSON.parse(sessionStorage.getItem('DHLResult')) || '');
    const [Fedexresult, setFedexResult] = useState(JSON.parse(sessionStorage.getItem('FedexResult')) || '');

    const [jploadloading, setJapanPostLoading] = useState(false);
    const [dhlloading, setDHLoading] = useState(false);
    const [fedexloading, setFedexLoading] = useState(false);
    
    const [cardsError, setCardsError] = useState(false);
    const [usZipError, setUsZipError] = useState(false);
    const [japanZipError, setJapanZipError] = useState(false);
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      
      const cardsValid = /^[1-9]\d*$/.test(cards);
      const usZipValid = /^\d{5}$/.test(usZip);
      const japanZipValid = /^\d{3}-\d{4}$/.test(japanZip);

      setCardsError(!cardsValid);
      setUsZipError(!usZipValid);
      setJapanZipError(!japanZipValid);

      if (!cardsValid || !usZipValid || !japanZipValid) {
        return;
      }

      setJapanPostLoading(true); // Start loading
      try{
        const response = await fetch('http://localhost:5000/api/shipping_japan_post', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cards, usZip, japanZip }),
          });
        
          const data = await response.json();
          setJapanResult(data);
          sessionStorage.setItem('japanPostResult', JSON.stringify(data));
      } catch (error){
        console.error("Error fetching data:",  error);
      }finally{
        setJapanPostLoading(false);
      }

      setDHLoading(true);
      try{
        const response = await fetch('http://localhost:5000/api/shipping_DHL', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cards, usZip, japanZip }),
          });
        
          const data = await response.json();
          setDHLResult(data);
          sessionStorage.setItem('DHLResult', JSON.stringify(data));
      } catch (error){
        console.error("Error fetching data:",  error);
      }finally{
        setDHLoading(false);
      }

      setFedexLoading(true);
      try{
        const response = await fetch('http://localhost:5000/api/shipping_Fedex', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cards, usZip, japanZip }),
          });
        
          const data = await response.json();
          setFedexResult(data);
          sessionStorage.setItem('FedexResult', JSON.stringify(data));
      } catch (error){
        console.error("Error fetching data:",  error);
      }finally{
        setFedexLoading(false);
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

    const ImageBox = styled(Box)(({ theme }) => ({
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '200px', // Set a fixed height for the image container
      width: '200px', // Set a fixed width for the image container
      overflow: 'hidden', // Hide the overflowing content
    }));

    const StyledImage = styled('img')({
      width: '100%',
      maxHeight: '100%', // Set a max height to scale the image proportionally
      objectFit: 'contain', // Maintain the aspect ratio while resizing
    });
    

    return (
      <Container maxWidth="md">
        <Box mt={4} mb={4}>
          <Typography variant="h4" align="center">
            Shipping Page
          </Typography>
        </Box>
        <Paper>
          <Box p={4}>
            <form onSubmit={handleSubmit}>
              <TextField
                label="Cards"
                value={cards}
                onChange={(e) => setCards(e.target.value)}
                fullWidth
                margin="normal"
                error={cardsError}
                helperText={cardsError ? 'Please enter a valid number' : ''}
              />
              <TextField
                label="US Zip Code"
                value={usZip}
                onChange={(e) => setUsZip(e.target.value)}
                fullWidth
                margin="normal"
                error={usZipError}
                helperText={usZipError ? 'Please enter a 5-digit US zip code' : ''}
              />
              <TextField
                label="Japan Zip Code"
                value={japanZip}
                onChange={(e) => setJapanZip(e.target.value)}
                fullWidth
                margin="normal"
                error={japanZipError}
                helperText={japanZipError ? 'Please enter a valid Japan zip code (xxx-xxxx)' : ''}
              />
              <Box mt={2}>
                <Button type="submit" variant="contained" color="primary">
                  Submit
                </Button>
              </Box>
            </form>
          </Box>
        </Paper>
        <Box mt={4}>
          {[{ image: japanPostImage, loading: jploadloading, renderResult: renderJapanResult }, { image: DHLImage, loading: dhlloading, renderResult: renderDHLResult }, { image: FedexImage, loading: fedexloading, renderResult: renderFedexResult }].map((item, index) => (
            <Paper key={index} sx={{ mb: 4 }}>
              <Box display="flex">
                <ImageBox>
                <StyledImage src={item.image} alt="Shipping Company" />
                </ImageBox>
                <Box flexGrow={1} p={2}>
                  {item.loading ? (
                    <Box display="flex" justifyContent="center">
                      <CircularProgress />
                    </Box>
                  ) : (
                    item.renderResult()
                  )}
                </Box>
              </Box>
            </Paper>
          ))}
        </Box>
      </Container>
    );
  };
    
    export default ShippingPage;