const fs = require('fs');
const Mun = require('./mun');
const db = require('../../models/dao');

module.exports = class State {

    /**
     * 
     * @param {String} parentPath Location of the parent directory
     * @param {String} name Abbrevation of the state name
     */
    constructor(parentPath, name) {
        this.parentPath = parentPath;
        this.name = name;
    }

    async loadMun() {
        const c = await db.connect();
        let arr = fs.readdirSync(`${this.parentPath}/${this.name}`)
        for (let i = 0; i < arr.length; i++) {
            if (arr[i].match('\.csv')) {
                let mun = new Mun(`${this.parentPath}/${this.name}`, arr[i]);
                mun.setState(this.name);
                await mun.readFile(c);
            }            
        }
        c.end();
    }
}