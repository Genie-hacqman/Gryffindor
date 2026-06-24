

import back from './assets/backend-development-64.png'
import React from 'react'
import Video from './components/Video.jsx'


function App(){
  const station = 'LocalStreamGh';

  return (
    <React.Fragment>
      <h1>welcome</h1>
      <p>{station}</p>

      <Video  channelname='adepa tv' />
     

    </React.Fragment>
  )
};

export default App