document.cookie = "0"

let cards = []
let sum = 0
let hasBlackJack = false
let isAlive = false
let message = ""
let messageEl = document.getElementById("message-el")
let cardsEl = document.getElementById("cards-el")
let sumEl = document.getElementById("sum-el")
let player = {
    name: "Player#000",
    chips: 145,
}
let playerEl = document.getElementById("player-el")
let newCardBtn = document.getElementById("newcard-btn")
newCardBtn.disabled = !isAlive

playerEl.textContent = `${document.cookie} points`

function getRandomCard() {
    let randomNumber = Math.floor(Math.random()*13) + 1
    if (randomNumber> 10){
        return 10
    } else if (randomNumber === 1) {
        return 11
    } else {
        return randomNumber
    }
}

function startGame() {
    isAlive = true
    let firstCard = getRandomCard()
    let secondCard = getRandomCard()
    cards = [firstCard, secondCard]
    sum = firstCard + secondCard
    newCardBtn.disabled = !isAlive
    renderGame()
}

function renderGame(){
    cardsEl.textContent = "Cards: " 
    for (let i = 0; i < cards.length; i++) {
        cardsEl.textContent += cards[i] + " "
    }
    sumEl.textContent = "Sum: " + sum
    if (sum < 21) {
        message = "Want to draw a new card?"
     } else if (sum === 21) {
         message = "You've got Blackjack!"
         hasBlackJack = true
         document.cookie = `${Number(document.cookie) + 10}`
         playerEl.textContent = `${document.cookie} points`

     } else {
         message = "You're out of the game!"
         isAlive = false
     }     
     messageEl.textContent = message
}

function newCard() {
    if (isAlive === true || hasBlackJack === true){
        let card = getRandomCard()
        sum += card
        cards.push(card)
        renderGame()
    }   
}



