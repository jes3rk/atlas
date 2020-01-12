const Pool = require('pg').Pool;

class Dao {
    constructor() {
        this.pool = new Pool({
            user: 'postgres',
            password: 'psql',
            host: 'localhost',
            port: '5432',
            database: 'atlas'
        })
        this.pool.connect().then(res => {
            console.log('db exists');
            res.end();
        }).catch(err => {
            // console.log(err);
            console.log('db doesn\'t exist. Creating...');
            const p = new Pool({
                user: 'postgres',
                password: 'psql',
                host: 'localhost',
                port: '5432',
                database: 'postgres'
            })
            p.query('CREATE DATABASE atlas', (err, res) => {
                if (err) throw err;
                console.log('atlas db created');
            })
            p.end();
        })
    }
    /**
     * 
     * @param {String} name Name of the table to be created
     * @param {Array} colArr Array of column types in raw SQL format
     */
    createTable(name, colArr) {
        this.pool.query(`CREATE TABLE ${name} (${colArr.join()})`, (err, res) => {
            if (err) throw err;
        })
    }

    insertBuffer(table, arr) {
        if (arr > 0) {
            this.pool.connect().then(c => {
                c.query('SELECT column_name FROM information_schema.columns WHERE table_name = $1 AND column_name != \'id\'', [table]).then(res => {
                    // console.log(res.rows.map(r => {
                    //     return `\"${r.column_name}\"`;
                    // }));
                    let query = `INSERT INTO ${table} (${res.rows.map(r => {
                        return `${r.column_name}`;
                    })}) VALUES ${arr.map(b => {
                        return `(${b.map(v => {
                            if (typeof v === "string") {
                                return `\'${v}\'`;
                            } else {
                                return v;
                            }
                        })})`
                    }).join()}`;
                    console.log(query);
                    c.query(query).then(() => {
                        c.end()
                    }).catch(err => {throw err});
                }).catch(err => {throw err})
            });
        }
    }
}

// const d = new Dao();
// d.insertBuffer('nj');
module.exports = Dao;