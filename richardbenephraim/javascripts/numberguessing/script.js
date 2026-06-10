


const url = 'https://newsapi.org/v2/top-headlines?'+
'country=us&'+
'apiKey=9084401e024a466c84f99f08e13f792c'


async function getdata() {

    const data = await fetch(url)
    .then((res) => res.json())
    console.log(data)

    for(const article of data.articles){
        console.log(article.title)

        
        
    };

}

getdata()





