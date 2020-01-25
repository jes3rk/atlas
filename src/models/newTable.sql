CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    lat NUMERIC,
    lon NUMERIC,
    street VARCHAR(64),
    city VARCHAR(32),
    state VARCHAR(2),
    zip VARCHAR(5)
)