const url = "https://newsapi.org/v2/everything?q=Apple&from=2026-06-09&sortBy=popularity&apiKey=9355e32231984a7488b9f4c769d0be94"
// const data = fetch(url)


// async function getdata() {
//         console.log("first")
//     const data = await fetch(url)
//     .then((res)=> res.json() )
//     console.log(data)
//         console.log("done")
// }
// getdata()


// function data() {
//     console.log("first")
//     const data = fetch(url)
//     .then((res)=> res.json())
//     console.log(data)
//     console.log("done fetching")
// }
// data()


// Your assignment
//  .use the newapi but this time us the other available route and display the list inside the browser using getdocumentbyID and map(), fetch etc

const url2 = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=9355e32231984a7488b9f4c769d0be94"
async function getinfo() {
    const data = await fetch(url2)
    .then((res)=> res.json())
    console.log(data.articles)
    const newsContainer = document.getElementById("html")
    data.articles.map((article) => {
        const newsItem = document.createElement("div")
        newsItem.className = "news-item"
        newsItem.innerHTML = `
            <h3>${article.title}</h3>
            <p>${article.description}</p>
            <a href="${article.url}" target="_blank">Read more</a>
        `
        newsContainer.append(newsItem)
    })
}
getinfo()   