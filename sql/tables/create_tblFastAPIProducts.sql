CREATE TABLE tblFastAPIProducts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    external_product_id INT NOT NULL UNIQUE,
    title VARCHAR(500) NOT NULL,
    price DECIMAL(10,2),
    description TEXT,
    category VARCHAR(200),
    image_url TEXT,
    rating_rate DECIMAL(3,2),
    rating_count INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
