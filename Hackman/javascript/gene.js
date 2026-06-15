// const btn = document.getElementById("clickButton")
// const div = document.getElementById("brocode")


// const hexalist = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

// const randomColorarr = []

// for (let i = 0; i < 6; i++) {
//     const random = Math.floor(Math.random() * 16)
//     randomColorarr.push(hexalist[random])
//     console.log(randomColorarr)

// }
//     div.classList.toggle(`bg-[#${randomColorarr.join("")}]`)



// btn.addEventListener("click", () => {
//     console.log("i am clicked")
//     div.classList.add("bg-red-500")
// })


// const body= document.body
// const divElement= document.getElementById("brocode");
// divElement.style.backgroundColor="pink";
// const ddv= document.createElement("div")
// ddv.innerHTML= "hello world"
// body.appendChild(ddv)
// console.log(divElement.innerHTML)

const url = "https://newsapi.org/v2/everything?q=Apple&from=2026-06-09&sortBy=popularity&apiKey=9355e32231984a7488b9f4c769d0be94"
// const data = fetch(url)
// console.log(data)

async function getData() {
    const data = await fetch(url).then((res) => res.json())
    console.log(data)
}
getData()   

