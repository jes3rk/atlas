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
        if (isNaN(l) || this.lat === undefined) {
            return 0;
        } else {
            this.lat = l;
            return 1;
        }
    }

    validateLon() {
        let l = Number.parseFloat(this.lon);
        if (isNaN(l) || this.lon === undefined) {
            return 0;
        } else {
            this.lon = l;
            return 1;
        }
    }

    validateStreet() {
        if (this.number !== "" && this.street !== "" && this.street !== undefined && this.number !== undefined) {
            return 1;
        } else {
            return 0;
        }
    }

    validateCity(d) {
        if (this.city === "" || this.city === undefined) {
            if (d === 'statewide') {
                if (this.district !== undefined) {
                    this.city = this.district;
                } else {
                    return 0;
                }
            } else {
                let arrD = d.split('_');
                arrD.shift();
                arrD.shift();
                arrD.forEach(w => {
                    return w.substring(0, 1).toUpperCase() + w.substring(1);
                })
                this.city = arrD.join(' ');
            }
        }
        return 1;
    }

    validateState(s) {
        if (this.state === "" || this.state === undefined) {
            this.state = s.toUpperCase();
        }
        return 1;
    }

    validateZip() {
        if (this.zip !== undefined && this.zip.length >= 5) {
            this.zip = this.zip.substr(0, 5);
            return 1;
        } else {
            0;
        }
    }

    toInsert() {
        return [
            this.lat,
            this.lon, 
            this.number + " " + this.street,
            this.city,
            this.state,
            this.zip
        ]
    }
}

module.exports = Address