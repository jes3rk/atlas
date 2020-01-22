const Pool = require('pg').Pool;

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
    })
}

module.exports = {
    connect: connect,
    initDB: initDB
}