const Address = require('../models/address');

class State {
    constructor(path) {
        this.path = path;
        this.writer = require('fs');
    }

    parseMun() {
        this.writer.readdir(this.path, (err, contents) => {
            contents.forEach(c => {
                if (this._getFileType(c) === 'csv') {
                    let m = new Mun(this.path + '/' + c);
                    m.import();
                }
            })
        })
    }

    _getFileType(name) {
        let arr = name.split('.');
        return arr[arr.length - 1];
    }
}

class Mun {
    constructor(path) {
        this.path = path;
        this.writer = require('fs');
        console.log(path);
    }

    import() {
        this.writer.readFile(this.path, {encoding: 'utf8'}, (err, data) => {
            let rawAddr = data.split('\n');
            rawAddr.shift();
            let allAddr = rawAddr.filter(a => {
                // return Address.fromCSV(a);
                let addr = Address.fromCSV(a);
                if (addr) {
                    
                } else {
                    return false;
                }
            })
            // console.log(allAddr.length);
        })
    }
}

module.exports = State;