import React, { useEffect, useState } from 'react'
import axios from "axios";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import Loader from '../components/Loader';
import Title from './Title';
import { Box, Toolbar, Container, Grid, Paper } from '@mui/material';
// Generate Order Data
// function createData(id, col1, col2, amount) {
//   return { id, col1, col2, amount };
// }

// const rows = [
//   createData(
//     0,
//     '16 Mar, 2019',
//     'Elvis Presley',
//     312.44,
//   ),
//   createData(
//     1,
//     '16 Mar, 2019',
//     'Paul McCartney',
//     866.99,
//   ),
//   createData(2, '16 Mar, 2019', 'Tom Scholz', 100.81),
//   createData(
//     3,
//     '16 Mar, 2019',
//     'Michael Jackson',
//     654.39,
//   ),
//   createData(
//     4,
//     '15 Mar, 2019',
//     'Bruce Springsteen',
//     212.79,
//   ),
// ];

const Stats = () => {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // testing
    // const myData = [
    //   { "title": "Title 1", "col1": 1, "col2": 7 },
    //   { "title": "Title 2", "col1": 2, "col2": 8 , "col3":13},
    //   { "title": "Title 3", "col1": 3, "col2": 9 },
    //   { "title": "Title 4", "col1": 4, "col2": 10 , "col3":1, "col4":2},
    //   { "title": "Title 5", "col1": 5, "col2": 11 },
    //   { "title": "Title 6", "col1": 6, "col2": 12 },
    // ]
    // setData(myData);

    // test data
    
  //   const myData = {
  //     "stats1": {
  //         "Count": [
  //             "8",
  //             "6",
  //             "6",
  //             "5",
  //             "5",
  //             "5",
  //             "4",
  //             "4",
  //             "4",
  //             "4",
  //             "4",
  //             "3",
  //             "3",
  //             "3",
  //             "3",
  //             "3",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "2",
  //             "1",
  //             "1",
  //             "1",
  //             "1",
  //             "1",
  //             "1",
  //             "1",
  //             "1"
  //         ],
  //         "Location": [
  //             "132",
  //             "233",
  //             "239",
  //             "138",
  //             "238",
  //             "263",
  //             "161",
  //             "166",
  //             "170",
  //             "237",
  //             "79",
  //             "107",
  //             "114",
  //             "148",
  //             "236",
  //             "68",
  //             "137",
  //             "141",
  //             "142",
  //             "162",
  //             "246",
  //             "249",
  //             "262",
  //             "43",
  //             "48",
  //             "50",
  //             "90",
  //             "113",
  //             "164",
  //             "211",
  //             "234",
  //             "4",
  //             "45",
  //             "7",
  //             "70"
  //         ],
  //         "Title": "Popular Pickup Locations"
  //     },
  //     "stats7": {
  //         "Count": [
  //             "100"
  //         ],
  //         "Month": [
  //             "01"
  //         ],
  //         "Title": "Total Trips per Month"
  //     }
  // }
  // setData(myData);

    // fetch data from backend
    setIsLoading(true);

    axios.get("/stats")
      .then(res => {setData(res.data); setIsLoading(false)})
      .catch(err => {console.log(err); setIsLoading(false)})
  }, []);

  
  // console.log(data);



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
      {isLoading ? <Loader/> : null}
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>Statistics</Typography>
        <Grid container spacing={3}>
          {/* Chart */}
          {/* <Grid item xs={12} md={8} lg={9}>
            <Paper
              sx={{
                p: 2,
                display: 'flex',
                flexDirection: 'column',
                height: 240,
              }}
            >
              <Chart />
            </Paper>
          </Grid> */}
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
          {/* Recent Orders */}
          {Object.keys(data).map((d, index) => <Grid item xs={12}>
            <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
              <Title>{data[d].Title}</Title>
              <Table size="medium">
                <TableHead>
                  <TableRow>
                    {Object.keys(data[d]).filter(k => k !== "Title").reverse().map((key) => <TableCell key={key}>{key}</TableCell>)}
                  </TableRow>
                </TableHead>
                <TableBody>
                  {/* {console.log(Object.keys(data[d]).filter(k => k !== "Title"))} */}
                    {data[d][Object.keys(data[d]).filter(k => k !== "Title")[0]].map((k, index) => <TableRow key={k}>
                      {Object.keys(data[d]).filter(k => k !== "Title").reverse().map((item) => <TableCell key={item}>{data[d][item][index]}</TableCell>)}
                    </TableRow>)}
                </TableBody>
              </Table>
            </Paper>
          </Grid>)}
        </Grid>
      </Container>
    </Box>
  )
}

export default Stats