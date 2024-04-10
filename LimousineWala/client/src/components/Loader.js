import React from 'react'
import { CircularProgress } from '@mui/material'

const Loader = () => {
  return (
    <div style={{display:'grid',placeItems:'center',height:'100vh',width:'100vw',position:'fixed',zIndex:10000,background:'rgba(0,0,0,0.5)'}}>
        <CircularProgress size='10rem'>
        </CircularProgress>
    </div>
  )
}

export default Loader