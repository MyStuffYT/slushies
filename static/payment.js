const ptext = document.getElementById("paymenttext")

setInterval(() => {
    fetch("/catfact").then(res=>res.text()).then(data=>ptext.innerText=data)
}, 4000)