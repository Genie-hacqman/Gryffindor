import {Routes, Route} from "react-router-dom"
import Landingpage from "./pages/landingpage";
import Homepage from "./pages/homepage";
import TvShows from "./pages/tvshows";

const App = () => {
  
  return (
    
    <>
    <Routes>
    <Route  path="/" element={<Landingpage />}/>
    <Route path="/home" element={<Homepage />} />
    <Route path="/tvshows" element={<TvShows/>} />
    
    </Routes>
    
    </>
  )
};

export default App;