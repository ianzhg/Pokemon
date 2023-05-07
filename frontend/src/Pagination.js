import React from 'react';
import { Pagination as MuiPagination } from '@mui/material';

const Pagination = ({ count, page, onChange }) => {
  return (
    <MuiPagination
      count={count}
      page={page}
      onChange={onChange}
      color="primary"
      size="large"
    />
  );
};

export default Pagination;
