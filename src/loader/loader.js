const db = require('../models/dao');
const Region = require('./classes/region');
/**
 * 
 * @param {Array<String>} regions Array of regions corresponding to the OpenAddresses system 
 */
async function load(regions) {
    await db.initDB();
    const rootUrl = 'https://data.openaddresses.io/openaddr-collected-us_';
    console.log('beginning download');
    for (let i = 0; i < regions.length; i++) {
        const reg = new Region(regions[i]);
        // await reg.download(rootUrl);
        // await reg.unpack();
        await reg.generateStates();
    }
}



load(['northeast']);