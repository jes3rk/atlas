const Pool = require('pg').Pool;
const fs = require('fs');

const p = new Pool({
    user: 'postgres',
    password: 'psql',
    host: 'localhost',
    port: '5432',
    database: 'atlas'
})

async function connect() {
    let res = await p.connect().catch(async (error) => {
        console.log('need to make db');
        await initDB();
        return connect();
    })
    return res;
}

async function initDB() {
    const np = new Pool({
        user: 'postgres',
        password: 'psql',
        host: 'localhost',
        port: '5432',
        database: 'postgres'
    })
    await np.query('CREATE DATABASE atlas').then(async () => {
        await np.end();
        let conn = await connect();
        await conn.query(fs.readFileSync('src/models/newTable.sql').toString());
        await conn.end();
    })
}

async function pushArr(arr) {
    let query = `INSERT INTO addresses (lat, lon, street, city, state, zip) VALUES (${arr.join()});`;
    console.log(query);
    // const conn = await connect();
    // await conn.query(query);
    // await conn.end();
}

module.exports = {
    connect: connect,
    initDB: initDB,
    loadData: pushArr
}