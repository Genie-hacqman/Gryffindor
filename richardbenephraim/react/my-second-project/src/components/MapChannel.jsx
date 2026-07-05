

const Channel = ()=>{
const stations = [
    "fish tv", "channel 247", "peace fm", "Localstreamgh tv", "Ahenfie tv", "mabesh tv"
]
    return(
        <div>

<section>
    <h1>tv station</h1>
    <div>
        <p>{stations.map((station) =>{
            <p>{station}</p>
        })}</p>
    </div>
</section>
        </div>
    )
};

export default Channel;