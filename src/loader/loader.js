class Loader {
    dataDir = 'data';
    baseURL = "https://data.openaddresses.io/";
    writer = require('fs');
    axios = require('axios');

    constructor(regArr) {
        this.regions = regArr;
    }

    _createURL(str) {
        return this.baseURL + `openaddr-collected-us_${str}.zip`;
    }

    downloadRegions() {
        if (!this.writer.existsSync(this.dataDir)) {
            this.writer.mkdirSync(this.dataDir);
        }
        this.regions.forEach(e => {
            this.axios({
                method: 'get',
                url: this._createURL(e),
                responseType: 'stream'
            }).then(response => {
                let stream = this.writer.createWriteStream(`${this.dataDir}/${e}.zip`);
                response.data.pipe(stream);
                stream.on('close', () => {
                    console.log(`Finished downloading reegion: ${e} -- unzipping`);
                }) 
            })
        });
    }
}

const l = new Loader(['northeast']);
l.downloadRegions();