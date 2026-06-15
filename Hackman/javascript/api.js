const url = "https://newsapi.org/v2/everything?q=Apple&from=2026-06-09&sortBy=popularity&apiKey=9355e32231984a7488b9f4c769d0be94"
// const data = fetch(url)


async function getdata() {
        console.log("first")
    const data = await fetch(url)
    .then((res)=> res.json() )
    console.log(data)
        console.log("done")
}
getdata()


// function data() {
//     console.log("first")
//     const data = fetch(url)
//     .then((res)=> res.json())
//     console.log(data)
//     console.log("done fetching")
// }
// data()