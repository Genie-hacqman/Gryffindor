

import back from './assets/backend-development-64.png'
import React from 'react'
import Video from './components/Video.jsx'


export default function App(){
  const station = 'LocalStreamGh';

  return (
    <React.Fragment>
      <h1>welcome</h1>
      <p>{station}
        <img src={back} alt="" srcset="" />
      </p>

      <Video  channelname='adepa tv' channelid='45123'  />
     

    </React.Fragment>
  )
};