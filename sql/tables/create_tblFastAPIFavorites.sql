CREATE TABLE tblFastAPIFavorites (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    product_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, product_id),
    FOREIGN KEY (product_id) REFERENCES tblFastAPIProducts(id) ON DELETE CASCADE
);
