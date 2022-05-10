const express = require('express')
const app = express()
const port = 3000

var os = require('node-os-utils');

var cpu = os.cpu
var ram = os.mem
var disk = os.drive

setInterval(() => {
cpu.usage()
  .then(info => {
    console.log("CPU:" + info)
  })
ram.info()
  .then(info => {
      console.log("RAM:" + info.usedMemPercentage)
  })
disk.info()
  .then(info => {
      console.log("DISK USED:" + info.usedPercentage)
  })
}, 1000);


app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})