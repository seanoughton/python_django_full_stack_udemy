// var myheader = document.querySelector("h1")
//
// myheader.style.color = "green"

var myheader = document.querySelector("h1")

function getRandomColor(){
  let letters = "0123456789ABCDEF"
  let color = "#"
  for (var i=0; i<6;i++){
    color += letters[Math.floor(Math.random()*16)]
  }
  return color
}

function changeHeaderColor(){
  colorInput = getRandomColor()
  myheader.style.color = colorInput
}

// myheader.style.color = getRandomColor()
setInterval("changeHeaderColor()",500)
