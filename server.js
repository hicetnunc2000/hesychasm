const methods = require('./methods')
const express = require('express')
const cors = require('cors')
const multer = require('multer')
var upload = multer()
const app = express()

app.use(express.json());       // to support JSON-encoded bodies
app.use(express.urlencoded()); // to support URL-encoded bodies
app.use(cors({ optionSuccessStatus: 200 }));

app.get('/' , (req, res) => {
    res.json({
        git : 'https://github.com/hicetnunc2000/ipfs-micro'
    })
})

app.post('/get_json', (req, res) => {
    methods.get(req.body.hash, res)
})

app.post('/get_list', (req, res) => {
    methods.getList(req.body.list, res)
})

app.post('/post_json', (req, res) => {
    methods.post(req.body, res)
})

app.post('/post_file', upload.any(), (req, res) => {
    methods.post_file(req.files[0].buffer, res)
})

var listener = app.listen(process.env.PORT || 3000, () => {
    console.log('*** console: listening on port ' + listener.address().port);
})