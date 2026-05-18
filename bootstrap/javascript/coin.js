function flipCoin(){
    return new Promise((resolve, reject) => {
        let result="tails"
        if (result == "heads"){
            resolve("you win")
        }
                    else {
                reject("you lose")
            }
    })
}

flipCoin().then((msg)=> {console.log(msg)})
.catch((err)=> {console.log(err)})