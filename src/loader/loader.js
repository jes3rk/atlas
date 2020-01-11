const Region = require('./region.js');

class Loader {
    dataDir = 'data';
    baseURL = "https://data.openaddresses.io/";
    writer = require('fs');
    axios = require('axios');
    unzipper = require('unzipper');

    constructor(regArr) {
        this.regions = regArr;
    }

    _createURL(str) {
        return this.baseURL + `openaddr-collected-us_${str}.zip`;
    }

    _downloadRegion(e) {
        this.axios({
            method: 'get',
            url: this._createURL(e),
            responseType: 'stream'
        }).then(response => {
            const path = `${this.dataDir}/${e}.zip`;
            let stream = this.writer.createWriteStream(path);
            response.data.pipe(stream);
            stream.on('close', () => {
                console.log(`Finished downloading region: ${e} -- unzipping`);
                this.writer.createReadStream(path)
                    .pipe(this.unzipper.Extract({ path: `${this.dataDir}/${e}`}))
                    .on('close', () => {
                        console.log(`Done extracting region: ${e}`)
                        this.writer.unlink(path, 
                            () => console.log(`Removed ${path}`));
                    });
            }) 
        }).catch(err => {
            console.log(err);
        });
    }

    downloadRegions() {
        console.log("Running download");
        if (!this.writer.existsSync(this.dataDir)) {
            this.writer.mkdirSync(this.dataDir);
        }
        this.regions.forEach(e => {
            this._downloadRegion(e);
        });
    }

    loadRegions() {
        this.regions.forEach(r => {
            const reg = new Region(r, this.dataDir);
            reg.parseFiles();
        })
    }
}


const l = new Loader(['northeast']);
// l.downloadRegions();
l.loadRegions();
