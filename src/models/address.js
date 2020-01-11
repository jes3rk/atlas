class Address {
    lat = 0.0000;
    lon = 0.0000;
    number = "";
    street = "";
    city = "";
    district = "";
    state = "";
    zip = "";

    static fromCSV(raw) {
        let s = raw.split(',');
        if (s.length > 7) {
            let a = new Address();
            a.lat = s[0];
            a.lon = s[1];
            a.number = s[2];
            a.street = s[3];
            a.city = s[5];
            a.district = s[6];
            a.state = s[7];
            a.zip = s[8];
            return a;
        } else {
            return false;
        }
    }

    validateLat() {
        let l = Number.parseFloat(this.lat);
        if (isNaN(l)) {
            return false
        } else {
            this.lat = l;
            return true;
        }
    }
}

module.exports = Address