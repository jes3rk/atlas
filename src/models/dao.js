const Pool = require('pg').Pool;
const fs = require('fs');

const initDB = () => {
    const primary = new Pool({
        user: "postgres",
        password: 'psql',
        host: 'localhost',
        port: '5432',
        database: 'postgres'
    })
    primary.query('CREATE DATABASE atlas', (err, res) => {
        console.log(res);
    })
    primary.query(fs.readFileSync('./src/models/sql/init.sql').toString(), (error, results) => {
        console.log(results);
        console.log(error);
    })
}

const db = new Pool({
    user: 'apollo',
    password: 'chariot',
    host: 'localhost',
    port: '5432',
    database: 'atlas'
})

// console.log(fs.readFileSync('./src/models/sql/init.sql').toString());
// initDB();
module.exports = db;