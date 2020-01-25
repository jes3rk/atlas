module.exports = class Address {
    constructor(rawInput) {
        this._isValid;
        this.rawArr = rawInput.split(',');
        this.defaults = {
            city: '',
            state: ''
        };
        if (this.rawArr.length >= 9) {
            this._isValid = true;
            this.lat = 0.0;
            this.lon = 0.0;
            this.number = "";
            this.street = "";
            this.city = "";
            this.zip = "";
        }
    }

    print() {
        const arr = [
            this.lat, 
            this.lon, 
            this.number, 
            this.street, 
            this.city,
            this.defaults.state,
            this.zip
        ];
        console.log(arr.join(" "))
    }

    isValid() {
        if (this._isValid) {
            let counter = 0;
            while (counter < 9 && this._isValid) {
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
                if (this._is(input)) {
                    this.number = input;
                    return true;
                } else {
                    return false;
                }
            case 3:
                if (this._is(input)) {
                    this.street = input;
                    return true;
                } else {
                    return false;
                }
            case 5:
                if (this._is(input)) {
                    this.city = input;
                    return true;
                } else {
                    this.city = this.defaults.city;
                    return true;
                }
            case 8:
                if (this._is(input)) {
                    this.zip = input;
                    return true;
                } else {
                    return false;
                }
            default:
                return true;
        }
    }

    _is(input) {
        if (input !== null && input !== undefined && input.length > 0) {
            return true;
        } else {
            return false;
        }
    }

    setDefaults(obj) {
        this.defaults = obj;
    }
}