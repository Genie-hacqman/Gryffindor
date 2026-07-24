import MuxPlayer from "@mux/mux-player-react";

const Videoplayer = ({url}) =>{
    return(
        <div>
        <MuxPlayer 
        src={url}
        playsInline
        muted
        style={{height:"100%", width:"100%"}}
        streamType="live"
        
        />
        
        </div>
    )
};


export default  Videoplayer;