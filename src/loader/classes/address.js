module.exports = class Address {
    constructor(rawInput) {
        this._isValid;
        this.rawArr = rawInput.split(',');
        if (this.rawArr.length >= 9) {
            this._isValid = true;
            this.lat = 0.0;
            this.lon = 0.0;
        }
    }

    isValid() {
        if (this._isValid) {
            let counter = 0;
            while (counter < 8 && this._isValid) {
                this._isValid = this._validator(counter, this.rawArr[counter]);
                counter++;
            }
            return this._isValid;
        } else {
            return false;
        }
    }

    /**
     * 
     * @param {Number} index 
     * @param {String} input 
     */
    _validator(index, input) {
        // lat, lon, number, street, unit, city, district, region, zipcode
        switch (index) {
            case 0:
                if (this._is(input)) {
                    try {
                        this.lat = Number.parseFloat(input);
                    } catch (error) {
                        return false;
                    }
                    return true;
                } else {
                    return false;
                }
            case 1:
                if (this._is(input)) {
                    try {
                        this.lon = Number.parseFloat(input);
                    } catch (error) {
                        return false;
                    }
                    return true;
                } else {
                    return false;
                }
            case 2:
                return this._is(input);
            case 3:
                return this._is(input);
            default:
                return true;
        }
    }

    _is(input) {
        if (input === null || input === undefined || input.length === 0) {
            return false;
        } else {
            return true;
        }
    }
}