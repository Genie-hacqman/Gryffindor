// console.log(document.querySelector('.header'), document.querySelector('#hard').textContent)

const dd = document.querySelector('#hard')


console.log(dd.textContent)

const addd = document.createElement('p')

dd.appendChild(addd)

console.log(dd)


const textin = document.textContent = 'this is a text'

addd.textContent = textin


addd.re