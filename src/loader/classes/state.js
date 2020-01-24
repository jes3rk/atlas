const fs = require('fs');
const Mun = require('./mun');

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
        fs.readdirSync(`${this.parentPath}/${this.name}`).forEach(m => {
            if (m.match('\.csv')) {
                let mun = new Mun(this.parentPath, m);
                mun.readFile();
            }            
        })
    }
}