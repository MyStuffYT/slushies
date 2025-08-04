const ptext = document.getElementById("paymenttext")

const jokes = setInterval(() => {
    fetch("/catfact").then(res=>res.text()).then(data=>ptext.innerText=data)
}, 10000)

const destroything = setInterval(()=>{
    ptext.innerText="Package destroyed. Reprocessing payment."
}, 35000)

setTimeout(()=>{
    clearInterval(jokes)
    clearInterval(destroything)
    ptext.innerText="The employees are too lazy to do work. Try again when the sun explodes."
},120000)