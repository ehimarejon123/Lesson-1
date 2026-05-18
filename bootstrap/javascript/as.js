function red(next){
    console.log("red light")
    next()
}

function green(next){
    console.log("green light")
    next()
}

function yellow(){
    console.log("yellow light")
    
}
red(()=> {
    green(()=> {
        yellow()
    })
})