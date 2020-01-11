class State {
    constructor(path) {
        this.path = path;
        this.writer = require('fs');
        console.log(this.path);
    }
}

module.exports = State;