const methods = require('./methods')
var express = require('express');
var cors = require('cors')
var app = express()

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

var listener = app.listen(process.env.PORT || 3000, () => {
    console.log('*** console: listening on port ' + listener.address().port);
})