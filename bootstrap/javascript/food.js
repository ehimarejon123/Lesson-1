function order(){
    return new Promise((resolve) => {
        setTimeout(()=> {
            resolve("food delivered")
        }, 3000)
    })
}
async function track() {
    console.log("Order placed")
    let result = await order ()
    console.log(result)
}
track()