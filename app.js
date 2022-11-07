const express = require('express');
const path = require('path')
const app = express()
const PORT = process.env.PORT || 5000;

app.use('/', express.static(path.join(__dirname, '/client')))

let reqPath = path.join(__dirname, '/client');
console.log(reqPath)
let errorPath = path.join(__dirname, '/client');

app.get('/', function(req, res) {
    res.sendFile(reqPath + '/index.html');
  });



// app.get('/', (req, res)=>{
//     res.sendFile(path.join(__dirname, 'client', 'index.html'))
// })

// app.get('/style.css', async (req, res)=>{
//     res.sendFile(path.join(__dirname, 'client/css', '/style.css'))
// })
//Set static folder
// app.use(express.static(path.join(__dirname, 'client')));

app.listen(PORT, () => console.log(` App is running on http://localhost:${PORT}`))
 