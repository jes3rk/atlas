const express = require('express');
const port = 3000;
const app = express()

app.get('/', (req, res) => res.sendfile('index.html'))

app.listen(port, () => {
    console.log(`App running on port ${port}`)
})