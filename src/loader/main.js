const db = require('../models/dao');

async function Main() {
    let con = await db.connect();
    console.log("hello world");
    con.end();
}

Main();