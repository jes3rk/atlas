const State = require('./state');

class Region {
    writer = require('fs');

    constructor(region, datadir) {
        this.path = datadir + '/' + region;
        this.filesDir = this.path + '/us';
    }

    parseFiles() {
        this.writer.readdir(this.filesDir, (err, contents) => {
            contents.forEach(f => {
                const s = new State(this.filesDir + '/' + f);
                s.parseMun();
            })
        })
    }
}

module.exports = Region;