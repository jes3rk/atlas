const assert = require('assert');

describe('Array', function() {
    describe('#indexOf()', function() {
        it('should return value of -1 if value is not present', function() {
            assert.equal([1,2,3].indexOf(4), -1);
        })
    })
})