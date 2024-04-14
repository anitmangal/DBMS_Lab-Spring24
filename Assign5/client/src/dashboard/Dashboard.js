import React, { useState, useEffect } from 'react'
import axios from "axios";
import Chart from './Chart';
import Deposits from './Deposits';
import { Box, Toolbar, Container, Grid, Paper, Stack, Chip, FormControl, InputLabel, Select, MenuItem, TextField, Button, Typography, Menu } from '@mui/material';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { columns, mapping } from './Data';
import Title from './Title';
import AddCircleRoundedIcon from '@mui/icons-material/AddCircleRounded';
import CancelRoundedIcon from '@mui/icons-material/CancelRounded';
import SearchIcon from '@mui/icons-material/Search';

function createData(id, date, name, shipTo, paymentMethod, amount) {
  return { id, date, name, shipTo, paymentMethod, amount };
}

const Dashboard = () => {
  const [rows, setRows] = useState([]);
  const [cols, setCols] = useState([]);
  const [allCols, setAllCols] = useState(columns);
  const [queries, setQueries] = useState([{ col: allCols[0], op: ">", val: 10 }]);

  useEffect(() => {
    console.log(queries);
  }, [queries]);

  const handleSearch = () => {
    const data = { cols, queries };
    console.log(data); 

    // const myData = [
    //   { "VendorID": 1, "extra": 2, "mta_tax": 3 },
    //   { "VendorID": 6, "extra": 4, "mta_tax": 5 },
    //   { "VendorID": 7, "extra": 8, "mta_tax": 9 },
    // ];
    // setRows(myData);



    axios.post("/", data)
      .then(res => { setRows(res.data);})
      .catch(err => console.log(err))

    // axios.get("/")
    //   .then(res => setRows(res.data))
    //   .catch(err => console.log(err)) 

    // useEffect( () => {
      // fetch("/", {method: "POST", body:JSON.stringify(data)})
    // },[]);

    // fetch("/", {method: "POST", body:JSON.stringify(data)});

  }

  return (
    <Box
      component="main"
      sx={{
        backgroundColor: (theme) =>
          theme.palette.mode === 'light'
            ? theme.palette.grey[100]
            : theme.palette.grey[900],
        flexGrow: 1,
        height: '100vh',
        overflow: 'auto',
      }}
    >
      <Toolbar />
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>Create Queries</Typography>
        <Grid container spacing={3}>
          {/* Recent Orders */}
          <Grid item xs={12}>
            <Paper
              sx={{
                p: 2,
                display: 'flex',
                flexDirection: 'column',
              }}
            >
              <Title>Available Columns</Title>
              <Stack direction={'row'} flexWrap={'wrap'}>
                {allCols.map(col =>
                  <Chip
                    sx={{ color: cols.includes(col) ? "white" : "black", backgroundColor: cols.includes(col) ? "primary.main" : "grey.300", mr: 2, mb: 2 }}
                    label={mapping[col]}
                    key={col}
                    onClick={() => setCols(cols => cols.includes(col) ? cols.filter(c => c !== col) : [...cols, col])}
                  />
                )}
              </Stack>
            </Paper>
          </Grid>

          {/* <Grid item xs={12}>
            <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', }}>
              <Title>Selected Columns</Title>
              <Stack direction={'row'} spacing={2} flexWrap={'wrap'}>
                {cols.map(col =>
                  <Chip
                    label={col}
                    key={col}
                    onClick={() => setCols(cols => cols.filter(c => c !== col))}
                    onDelete={() => setCols(cols => cols.filter(c => c !== col))}
                  />
                )}
              </Stack>
            </Paper>
          </Grid> */}

          <Grid item xs={12}>
            <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>

              <Title>Query</Title>
              <Table size="medium">
                <TableHead>
                  <TableRow>
                    <TableCell align="center">Sl No.</TableCell>
                    <TableCell>Column</TableCell>
                    <TableCell align="center">Operator</TableCell>
                    <TableCell align="center">Value</TableCell>
                    <TableCell align="center">Add</TableCell>
                    <TableCell align="center">Remove</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {queries.map((query, index) => (
                    <TableRow key={query}>
                      <TableCell align="center">{index + 1}</TableCell>
                      <TableCell>
                        <FormControl fullWidth>
                          <InputLabel>Column</InputLabel>
                          <Select
                            label="Column"
                            value={query.col}
                            onChange={(e) => setQueries(queries => {
                              if (!queries.find(q => q.col === e.target.value)) {
                                const myQuery = queries[index];
                                const updatedQueries = queries.filter((q, i) => i !== index);
                                updatedQueries.splice(index, 0, { ...myQuery, col: e.target.value });
                                return updatedQueries;
                              }
                              return queries;
                            })}
                          >
                            {allCols.map(col => <MenuItem value={col}>{col}</MenuItem>)}
                          </Select>
                        </FormControl>
                      </TableCell>
                      <TableCell align="center">
                        <FormControl fullWidth>
                          <InputLabel>Column</InputLabel>
                          <Select
                            value={query.op}
                            label="Column"
                            onChange={(e) => setQueries(queries => {
                              const myQuery = queries[index];
                              const updatedQueries = queries.filter((q, i) => i !== index);
                              updatedQueries.splice(index, 0, { ...myQuery, op: e.target.value });
                              return updatedQueries;
                            })}
                          >
                            <MenuItem value="<">{"<"}</MenuItem>
                            <MenuItem value=">">{">"}</MenuItem>
                            <MenuItem value="=">{"="}</MenuItem>
                            <MenuItem value="!">{"≠"}</MenuItem>
                          </Select>
                        </FormControl>
                      </TableCell>
                      <TableCell align="center">
                        <TextField label="Value" value={query.val} onChange={(e) => setQueries(queries => {
                          const myQuery = queries[index];
                          const updatedQueries = queries.filter((q, i) => i !== index);
                          updatedQueries.splice(index, 0, { ...myQuery, val: e.target.value });
                          return updatedQueries;
                        })} />
                      </TableCell>
                      <TableCell align="center"><AddCircleRoundedIcon sx={{ cursor: "pointer" }} color="success" onClick={() => setQueries(queries => [...queries, { col: allCols.filter(c => !queries.find(q => q.col === c))[0], op: ">", val: 10 }])} /></TableCell>
                      <TableCell align="center"><CancelRoundedIcon sx={{ cursor: "pointer" }} color="error" onClick={() => queries.length > 1 && setQueries(queries => queries.filter((q, i) => i !== index))} /></TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
              <Button variant="contained" startIcon={<SearchIcon />} onClick={() => handleSearch()} sx={{ m: "auto", mt: 2 }}>Search</Button>
            </Paper>
          </Grid>

          {rows?.length ? <Grid item xs={12}>
            <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
              <Title>Results</Title>
              <Table size="medium">
                <TableHead>
                  <TableRow>
                    <TableCell>Sl No.</TableCell>
                    {cols.map(col => <TableCell key={col}>{col}</TableCell>)}
                  </TableRow>
                </TableHead>
                <TableBody>
                  {rows.map((row, index) => (
                    <TableRow key={row}>
                      <TableCell>{index + 1}</TableCell>
                      {cols.map(col => <TableCell key={col}>{row[col]}</TableCell>)}
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Paper>
          </Grid> : null}


          {/* Recent Deposits */}
          {/* <Grid item xs={12} md={4} lg={3}>
            <Paper
              sx={{
                p: 2,
                display: 'flex',
                flexDirection: 'column',
                height: 240,
              }}
            >
              <Deposits />
            </Paper>
          </Grid> */}

          {/* Chart */}
          {/* <Grid item xs={12}>
            <Paper
              sx={{
                p: 2,
                display: 'flex',
                flexDirection: 'column',
                height: 240,
                // mx:16
              }}
            >
              <Chart />
            </Paper>
          </Grid> */}
        </Grid>
      </Container>
    </Box>
  )
}

export default Dashboard