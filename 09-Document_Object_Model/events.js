var one = document.querySelector("#one")
var two = document.querySelector("#two")
var three = document.querySelector("#three")

var button = document.querySelector("button")

function test(){
  console.log("test")
}

button.addEventListener("click",test)

one.addEventListener("mouseover",function(){
  one.innerHTML = " Mouse Currently Over"
  one.style.color = "red"
})

one.addEventListener("mouseout",function(){
  one.innerHTML = "HOVER OVER ME"
  one.style.color = "black"
})


two.addEventListener("click",function(){
  two.innerHTML = "Clicked"
  two.style.color = "red"
})


three.addEventListener("dblclick",function(){
  three.innerHTML = "Double Click"
  three.style.color = "red"
})
