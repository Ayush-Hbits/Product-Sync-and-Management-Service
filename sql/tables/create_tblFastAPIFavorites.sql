CREATE TABLE IF NOT EXISTS tblFastAPIFavorites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_user_product (user_id, product_id),
    CONSTRAINT fk_favorite_product
        FOREIGN KEY (product_id) REFERENCES tblFastAPIProducts(id)
        ON DELETE CASCADE
);
