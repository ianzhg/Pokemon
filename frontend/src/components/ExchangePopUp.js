import React, { useState } from 'react';
import {Dialog, DialogTitle } from '@mui/material';
import Drawer from '@mui/material/Drawer';
import PaidIcon from '@mui/icons-material/Paid';
import IconButton from '@mui/material/IconButton';
import CurrencyExchange from './ExchangeRate'

const CurrencyExchangeButton = () => {

  const [drawerOpen, setDrawerOpen] = useState(false);

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen);
  };

  return (
    <>
        <IconButton onClick={toggleDrawer}>
            <PaidIcon fontSize="large" />
        </IconButton>
        <Dialog>
            <DialogTitle>Currency Exchange</DialogTitle>
            <CurrencyExchange />
        </Dialog>
        <Drawer
            anchor="right"
            open={drawerOpen}
            onClose={toggleDrawer}
            >
            <CurrencyExchange />
        </Drawer>
    </>
  );
};

export default CurrencyExchangeButton;