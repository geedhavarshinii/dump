let hands = ['rock', 'paper', 'scissors']
let resultEl = document.getElementById("result-el")
let messageEl = document.getElementById("message-el")
let oppEl = document.getElementById("opp-el")
let winner = {
    rock: "scissors",
    paper: "rock",
    scissors: "paper"
}

messageEl.textContent = "You: Rock - Paper - Scissors"

function startGame(e) {
    let randomIndex = Math.floor(Math.random() * 3)
    let opp = hands[randomIndex]
    oppEl.textContent = "Opponent: " + opp
    if (opp == winner[e]) {
        resultEl.textContent = "You win!"
    } else if (winner[opp] == e) {
        resultEl.textContent = "You lose!"
    } else {
        resultEl.textContent = "It's a draw."
    }
}


//function getHand() {
   //return randomIndex
//}