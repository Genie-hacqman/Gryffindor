const computerChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')
const possibleChoices = document.querySelectorAll('button')
let userChoice; 
let computerChoice; 
let result

const choiceEmojis = {
    'rock': '👊',
    'sissors': '✌️',
    'papper': '✋'
}

const choiceNames = {
    'rock': 'Rock',
    'sissors': 'Scissors',
    'papper': 'Paper'
}

possibleChoices.forEach(possibleChoices => possibleChoices.addEventListener('click',(e) => {
    userChoice = e.target.id 
    userChoiceDisplay.innerHTML = `
        <div class="flex flex-col items-center gap-4">
            <span class="text-9xl animate-bounce">${choiceEmojis[userChoice]}</span>
            <span class="text-2xl font-bold text-blue-300">${choiceNames[userChoice]}</span>
        </div>
    `
    getComputerChoice();
    getResult();
}))

function getComputerChoice(){
    const randomNumber = Math.floor(Math.random() * 3)+1
    console.log(randomNumber)

    if(randomNumber === 1){
        computerChoice = 'rock'
    }
    if(randomNumber === 2){
        computerChoice = 'sissors'
    }
    if(randomNumber === 3){
        computerChoice = 'papper'
    }
    computerChoiceDisplay.innerHTML = `
        <div class="flex flex-col items-center gap-4">
            <span class="text-9xl animate-pulse">${choiceEmojis[computerChoice]}</span>
            <span class="text-2xl font-bold text-gray-300">${choiceNames[computerChoice]}</span>
        </div>
    `
}

function getResult(){
    if(computerChoice === userChoice){
        result = 'it is a draw'
    }
    if(computerChoice === 'rock' && userChoice === 'papper'){
        result = 'you win'
    }
    if(computerChoice === 'rock' && userChoice === 'sissors'){
        result = 'you lost'
    }
    if(computerChoice === 'papper' && userChoice === 'rock'){
        result = 'you lost'
    }
    if(computerChoice === 'papper' && userChoice === 'sissors'){
        result = 'you win'
    }
    if(computerChoice === 'sissors' && userChoice === 'papper'){
        result = 'you lost'
    }
    if(computerChoice === 'sissors' && userChoice === 'rock'){
        result = 'you win'
    }
    resultDisplay.innerHTML = result

}
