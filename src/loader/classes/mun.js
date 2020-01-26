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

    async readFile() {
        let raw = fs.readFileSync(`${this.parentPath}/${this.name}`, { encoding: 'utf8'});
        let broken = raw.split('\n');
        let validCount = 0;
        let buffer = [];
        let pushCount = 0;
        let conn = await db.connect();
        for (let i = 1; i < broken.length; i+=100) {
            let addr = new Address(broken[i]);
            addr.setDefaults({
                city: Mun.fixString(this.name),
                state: this.state
            })
            if (addr.isValid()) {
                await conn.query({
                    text: 'INSERT INTO addresses (lat, lon, street, city, state, zip) VALUES ($1, $2, $3, $4, $5, $6)',
                    values: addr.insert()
                })
                pushCount++;
                validCount++;
            }
        }
        
        console.log(`Found ${validCount} valid addresses for ${this.name} out of ${broken.length - 1} (${Math.floor((validCount / (broken.length - 1)) * 100)}%)`);
        console.log(`Pushed ${pushCount} addresses for ${this.name}`);
    }

    static fixString(input) {
        let plain = input.substring(0, input.lastIndexOf('.'));
        let arr = plain.split('_');
        if (arr[0] === 'city') {
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