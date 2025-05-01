"-- DB schema here" 
-- Creating a table to store components info
CREATE TABLE components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL,
    image_url TEXT
);

-- Sample data
INSERT INTO components (name, description, price, image_url) VALUES
('LED Bulb', 'Energy-efficient LED bulb for home use', 3.99, 'led_bulb.jpg'),
('Resistor', 'Standard 100 Ohm resistor', 0.02, 'resistor.jpg');
