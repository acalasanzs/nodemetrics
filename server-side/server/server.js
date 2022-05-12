const express = require('express');
const server = express();
const cors = require('cors');

server.use(express.json());
server.use(cors());
var data;
server.get("/", (req, res) => {
    res.send(data);
})
server.post('/data', (req, res) => {
    data = req.body.usage
    res.send("SUCCESSFUL")
    console.log(data)
});

server.listen(3000, () => console.log("Server started!"));