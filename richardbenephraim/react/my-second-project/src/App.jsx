import LikeButton from "./components/LikeButton";
import MapChannel from "./components/MapChannel"




const App = ()=>{

  const url = "https://localcodetech.pythonanywhere.com//api/channels"

  async function getData() {

    const data = await fetch(url).then((res)=>res.json)
    
  }

  return(
    <div>

<LikeButton />

<MapChannel />
    </div>
  )
};

export default App;
