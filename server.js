const express = require('express')
const path = require('path')

const port = process.env.PORT || 3080

const server = express()

server.use(express.static(path.join(__dirname, './client/out')))

server.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, './client/out/index.html'))
})

server.listen(port, (err) => {
    if (err) throw err
    console.log(`> Server ready on http://localhost:${port}`)
})