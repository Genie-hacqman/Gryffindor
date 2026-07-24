

const Channel = ()=>{
const stations = [
    "fish tv", "channel 247", "peace fm", "Localstreamgh tv", "Ahenfie tv", "mabesh tv"
];


return(
    <div>

        <section>
           {stations.map((station, index) =>{
            return(
                <h2 key={index}>
                    {station}
                </h2>
            )
           })}
        </section>
    </div>
)

};
export default Channel;