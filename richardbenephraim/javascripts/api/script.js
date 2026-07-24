
const url = "http://www.omdbapi.com/?i=tt3896198&apikey=2e30f5e2"
const url2 = "http://www.omdbapi.com/?t=rookie&apikey=2e30f5e26"


const div = document.querySelector("#check")

const divv = document.getElementById("checker")
console.log(divv)

div.addEventListener('click', getData)


async function getData () {
    
    const data = await fetch(url2)
    .then((response) =>{
        if (!response.ok) {
            throw new Error `error ${response.statusText}`
        }
        return response.json()

    }).then(res=>{
        console.log(res)
    })
.catch(error=> {
    console.error(`error ${error}`)
})
   
    
    }


    const obg= {
        name: "kwesi",
        age:23
    }


    const arr = [2,4,7];
    arr.map((ccc) =>{
        console.log(ccc+5)
    })