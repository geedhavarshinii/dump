let hands = ['Rock', 'Paper', 'Scissors']
let resultEl = document.getElementById("result-el")

function startGame() {
    let randomIndex = Math.floor(Math.random() * 3)
    let result = hands[randomIndex]
    resultEl.textContent = "Result: " + result
}

//function getHand() {
   //return randomIndex
//}