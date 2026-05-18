let cart = {
    item1 : {
        name:"Shoes",
        price: 3000 ,
    },
    item2 : {
        name: "glass",
        price: 4000 ,
    }
}
let jsonCart = JSON.stringify(cart)
let finalCart= JSON.parse(jsonCart)
console.log(finalCart)
console.log(
    finalCart.item1.price +
    finalCart.item2.price
)

