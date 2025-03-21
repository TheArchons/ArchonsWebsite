window.onload = function() {
    setInterval(() => {
        let currEpoch = new Date().getTime()/1000;
        currEpoch -= 1169539200;
        currEpoch /= 31556926;
        document.getElementById("age").innerHTML = currEpoch.toFixed(9);
    }, 10);
};