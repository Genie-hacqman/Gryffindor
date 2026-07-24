


const Logo =({logoUrl})=>{
    console.log(logoUrl)
    return(

        <div>
            <img src={logoUrl} alt="website logo" loading="lazy" width={"150"}/>
        </div>
    )
};

export default Logo;