const fs = require('fs');
const db = require('../../models/dao');
const Address = require('./address');

module.exports = class Mun {

    /**
     * 
     * @param {String} parentPath Path to the parent dir
     * @param {String} name Name of the municipality
     */
    constructor(parentPath, name) {
        this.parentPath = parentPath;
        this.name = name;
    }

    async readFile(conn) {
        let raw = fs.readFileSync(`${this.parentPath}/${this.name}`, { encoding: 'utf8'});
        let broken = raw.split('\n');
        let validCount = 0;
        let pushCount = 0;
        let buffer = [];
        for (let i = 1; i < broken.length; i++) {
            let addr = new Address(broken[i]);
            addr.setDefaults({
                city: Mun.fixString(this.name),
                state: this.state
            })
            if (addr.isValid()) {
                // await conn.query('INSERT INTO addresses (lat, lon, street, city, state, zip) VALUES ($1, $2, $3, $4, $5, $6)', addr.insert())
                pushCount++;
                buffer.push(`(${addr.print(',')})`);
                // validCount++;
                if (buffer.length > 1000 || i === broken.length - 1) {
                    await conn.query(`INSERT INTO addresses (lat, lon, street, city, state, zip) VALUES ${buffer.join()}`);
                    validCount += buffer.length;
                    buffer = [];
                }
            }
        }
        
        console.log(`Found ${validCount} valid addresses for ${this.name} out of ${broken.length - 1} (${Math.floor((validCount / (broken.length - 1)) * 100)}%)`);
        console.log(`Pushed ${pushCount} addresses for ${this.name}`);
    }

    static fixString(input) {
        let plain = input.substring(0, input.lastIndexOf('.'));
        let arr = plain.split('_');
        if (arr[0] === 'city' || arr[0] === 'town') {
            arr.shift();
            arr.shift();
        }
        return arr.map(s => {
            return s.substring(0, 1).toUpperCase() + s.substring(1);
        }).join(' ');
    }

    setState(s) {
        this.state = s.toUpperCase();
    }
}