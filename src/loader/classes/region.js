const fs = require('fs');
const axios = require('axios');

module.exports = class Region {
    /**
     * 
     * @param {String} region Name of the region to import
     */
    constructor(name) {
        this.name = name;
    }

    static async _download(rootUrl, region) {
        await new Promise(resolve => 
            axios({
                url:`${rootUrl}${region}.zip`,
                method: 'get',
                responseType: 'stream'
            }).then(res => {
                let stream = res.data.pipe(fs.createWriteStream(`data/${region}.zip`))
                stream.on('finish', resolve);
            })
        )
    }

    async download(rootUrl) {
        if (!fs.existsSync('data')) {
            fs.mkdirSync('data');
        }
        await Region._download(rootUrl, this.name);
        console.log(`${this.name} has been downloaded`);
    }
}