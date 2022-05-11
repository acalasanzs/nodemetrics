const express = require('express');
const server = express();
const cors = require('cors');

server.use(express.json());
server.use(cors());
var cpuUsage, ramUsage, diskUsage, gpuUsage;
var gpu = false;
server.get("/", (req, res) => {
    res.send("Hello World!");
})

server.post('/data', (req, res) => {
    if (req.body.usage.length > 3) {
        gpu = true;
        [cpuUsage, ramUsage, diskUsage, gpuUsage] = req.body.usage
    }else {
        [cpuUsage, ramUsage, diskUsage] = req.body.usage
    }
    res.send("SUCCESSFUL")
    console.log(cpuUsage, ramUsage, diskUsage, gpuUsage)
});

server.listen(3000, () => console.log("Server started!"));