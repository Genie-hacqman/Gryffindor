import {Routes, Route} from "react-router-dom"
import Landingpage from "./pages/landingpage";
import Homepage from "./pages/homepage";

const App = () => {
  
  return (
    
    <>
    <Routes>
    <Route  path="/" element={<Landingpage />}/>
    <Route path="/home" element={<Homepage />} />
    
    </Routes>
    
    </>
  )
};

export default App;