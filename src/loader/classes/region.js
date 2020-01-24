const fs = require('fs');
const axios = require('axios');
const unzip = require('unzip');
const State = require('./state');

module.exports = class Region {
    /**
     * 
     * @param {String} region Name of the region to import
     */
    constructor(name) {
        this.name = name;
    }

    /**
     * Private static function for downloading regions to a zip file in the data dir
     * @param {String} rootUrl Root url of the online data dir
     * @param {String} region Lowercase name of the region to download
     */
    static async _download(rootUrl, region) {
        await new Promise(resolve => 
            axios({
                url:`${rootUrl}${region}.zip`,
                method: 'get',
                responseType: 'stream'
            }).then(res => {
                let stream = res.data.pipe(fs.createWriteStream(`data/${region}.zip`))
                stream.on('finish', resolve);
            }).catch(err => {
                throw err;
            })
        )
    }

    /**
     * Private static function for unpacking a zip file in the data dir
     * @param {String} file Name of the region to unpack 
     */
    static async _unpack(file) {
        await new Promise(resolve => 
            fs.createReadStream(`data/${file}.zip`).pipe(unzip.Extract({
                path: `data/${file}`
            })).on('finish', resolve)
        )
    }

    /**
     * Public function for downloading this region to a zip file in the data dir
     * @param {String} rootUrl Root url fo the online data dir
     */
    async download(rootUrl) {
        if (!fs.existsSync('data')) {
            fs.mkdirSync('data');
        }
        await Region._download(rootUrl, this.name);
        console.log(`${this.name} has been downloaded`);
    }

    /**
     * Public function for unpacking this region from a zip file in the data dir and deleting the zip file after
     */
    async unpack() {
        await Region._unpack(this.name);
        // fs.unlinkSync(`data/${this.name}.zip`);
        console.log('unpacked');
    }

    async generateStates() {
        const statesDir = `data/${this.name}/us`;
        fs.readdirSync(statesDir).forEach(async s => {
            let state = new State(statesDir, s);
            await state.loadMun();
        })
        
    }
}