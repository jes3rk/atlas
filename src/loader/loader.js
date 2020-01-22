const db = require('../models/dao');
const Region = require('./classes/region');
/**
 * 
 * @param {Array<String>} regions Array of regions corresponding to the OpenAddresses system 
 */
async function load(regions) {
    // await db.initDB();
    const rootUrl = 'https://data.openaddresses.io/openaddr-collected-us_';
    console.log('beginning downloading');
    regions.forEach(async r => {
        const reg = new Region(r);
        await reg.download(rootUrl);
    })
}



load(['northeast']);