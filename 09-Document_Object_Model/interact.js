var p = document.querySelector('p')

p.textContent = "new text"
p.innerHTML = "newer text"

var special = document.querySelector("#special")

var specialanchor = special.querySelector("a")

specialanchor.style.color = "green"
specialanchor.innerHTML = "Amazon"
specialanchor.setAttribute("href","https://www.amazon.com")
