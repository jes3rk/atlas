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
        for (let i = 1; i < broken.length; i++) {
            let addr = new Address(broken[i]);
            addr.setDefaults({
                city: Mun.fixString(this.name)
            })
            if (addr.isValid()) {
                validCount++;
            }
            if (i === 1) {
                addr.print();
            }
        }
        console.log(`${validCount} valid addresses for ${this.name} out of ${broken.length - 1} (${Math.floor((validCount / (broken.length - 1)) * 100)}%)`);
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
}