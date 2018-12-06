// Cells
var cells = document.querySelectorAll("td")
let currentPlayer = "O"

function fill(){
  if (this.innerHTML !== " "){
    return
  }
  if (currentPlayer === "X"){
    this.innerHTML = "O"
    currentPlayer = "O"
  } else {
    this.innerHTML = "X"
    currentPlayer = "X"
  }

}

// [].forEach.call(cells,function(e){e.addEventListener('click',addO,false)})
for (let cell of cells){
  cell.addEventListener("click",fill)
}

// Btn restart
var btn = document.querySelector("button")
function restart(){
  for (let cell of cells){
    cell.innerHTML = " "
    currentPlayer = "O"
  }
}

btn.addEventListener("click",restart)
