CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    content TEXT
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    role INTEGER
);
CREATE TABLE opening_hours (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants
    day INTEGER,
    opening_time TEXT,
    closing_time TEXT
);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants,
    user_id INTEGER REFERENCES users,
    stars INTEGER,
    review TEXT
);
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants,
    group TEXT
);
