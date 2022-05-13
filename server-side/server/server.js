const express = require('express');
const server = express();
const cors = require('cors');
var path = require('path')
server.use(express.json());
server.use(cors());
var data;
server.get("/", (req, res) => {
    res.send(data);
});
server.use(express.static("dist"))
server.get("/visual", (req, res) => {
    res.sendFile(path.join('dist', 'index.html'), {root: '.'})
})
server.post('/data', (req, res) => {
    data = req.body.usage
    res.send("SUCCESSFUL")
});

server.listen(3001, () => console.log("Server started!"));