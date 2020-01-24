const fs = require('fs');

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
        fs.createReadStream(`${this.parentPath}/${this.name}`).pipe(s => {
            console.log(s);
        })
    }
}