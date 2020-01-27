CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    street VARCHAR(64),
    city VARCHAR(32),
    state VARCHAR(2),
    zip VARCHAR(5)
);

CREATE INDEX idx_addresses_city on addresses(city);
CREATE INDEX idx_addresses_state on addresses(state);
CREATE INDEX idx_addresses_zip on addresses(zip);