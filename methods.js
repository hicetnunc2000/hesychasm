const IPFS = require('ipfs-api');
var Promise = require('es6-promise').Promise;

const ipfs = new IPFS({
    host: 'ipfs.infura.io',
    port: 5001, protocol:
        'https'
});

module.exports = {

    get: async (hash, res) => {

        const obj = await ipfs.files.get(hash)
        res.json(JSON.parse(obj[0].content.toString('utf-8')))

    },

    getList: async (list, res) => {

        res.json({
            jsons: await Promise.all(list.map(async hash => {
                var obj = await ipfs.files.get(hash)
                return JSON.parse(obj[0].content.toString('utf-8'))
            }))
        })

    },

    post: async (data, res) => {

        var buffer = Buffer.from(JSON.stringify(data))
        var hash = await ipfs.files.add(buffer)
        
        res.json({
            hash: hash[0].hash
        })

    }

}

