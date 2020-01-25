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
            if (addr.isValid()) {
                validCount++;
            }
        }
        console.log(`${validCount} valid addresses for ${this.name} out of ${broken.length - 1} (${Math.floor((validCount / (broken.length - 1)) * 100)}%)`);
    }
}