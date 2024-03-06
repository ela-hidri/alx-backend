const redis = require("redis")
const client = redis.createClient();
import promisify from 'util'

const get = promisify(client.get).bind(client)
const set = promisify(client.set).bind(client)

const listProducts = [
    { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
    { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
    { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
    { id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
];
function getItemById(id) {
    return (listProducts.filter(Item=> Item.id === id));
}
const express = require('express')
const app = express();
const port = 1245

app.get('/list_products', (req, res)=>{
    res.json(listProducts)
})

app.get('/list_products/:itemId', async (req, res)=>{
    const itemId = parseInt(req.params.itemId)
    const item = getItemById(itemId)
    const currentReservedStock = await getCurrentReservedStockById(itemId);
  if (item) {
    item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
    res.json(item);
    return;
  }
  res.json({"status":"Product not found"});

})
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.json({"status":"Product not found"});
    }
    const currentReservedStock = await getCurrentReservedStockById(itemId);
    item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
    if ((item.stock - item.reservedStock) < 1) {
      res.json({"status":"Not enough stock available","itemId":itemId});
      return;
    }
    reserveStockById(itemId, Number(currentReservedStock) + 1);
    res.json({"status":"Reservation confirmed","itemId":itemId});
  });
app.listen(port)
function reserveStockById(itemId, stock){
    client.set(itemId, stock)
}
async function getCurrentReservedStockById(itemId){
    await get(itemId).then((stock)=> {return(stock)})
}