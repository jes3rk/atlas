const Address = require('../models/address');
const Dao = require('../models/dao');

const dao = new Dao();

class State {
    constructor(path) {
        this.path = path;
        this.writer = require('fs');
        let parr = this.path.split('/');
        this.state = parr[parr.length - 1];
        // dao.createTable(parr[parr.length - 1], [
        //     'id SERIAL PRIMARY KEY',
        //     'lat DOUBLE PRECISION',
        //     'lon DOUBLE PRECISION',
        //     'street VARCHAR(64)',
        //     'city VARCHAR(64)',
        //     'state VARCHAR(2)',
        //     'zip VARCHAR(5)'
        // ])
        dao.insertBuffer(this.state);
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
        let parr = path.split('/');
        this.state = parr[3];
        this.mun = parr[4].split('.')[0];
        console.log(path);
    }

    import() {
        this.writer.readFile(this.path, {encoding: 'utf8'}, (err, data) => {
            let rawAddr = data.split('\n');
            rawAddr.shift();
            console.log(`Initial length for ${this.path} is ${rawAddr.length}`);
            let allAddr = [];
            let validCount = 0;
            rawAddr.forEach(a => {
                let addr = Address.fromCSV(a);
                let count = 0;

                if (addr) {
                    count++;
                    count += addr.validateLat();
                    count += addr.validateLon();
                    count += addr.validateStreet();
                    count += addr.validateCity(this.mun);
                    count += addr.validateState(this.state);
                    count += addr.validateZip();
                }

                if (count === 7) {
                    validCount++; // use artifical limiter
                    if (validCount < 1000 || validCount % 3 === 0) {
                        allAddr.push(addr);
                    }
                    if (allAddr.length >= 1000) {
                        dao.insertBuffer(this.state, allAddr);
                        allAddr = [];
                    }
                }
                
            })
            dao.insertBuffer();
            console.log(`Final length of ${this.path} is ${allAddr.length}`);

        })
    }
}

module.exports = State;