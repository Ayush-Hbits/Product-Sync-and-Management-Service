from app.utils.stored_procedure import execute_sp


def upsert_product(db, product):

    execute_sp(
        db,
        "sp_UpsertProduct",
        {
            "p_external_product_id": product["id"],
            "p_title": product["title"],
            "p_price": product["price"],
            "p_category": product["category"],
            "p_description": product["description"],
            "p_image_url": product["image"],
            "p_rating_rate": product["rating"]["rate"],
            "p_rating_count": product["rating"]["count"]
        }
    )


    db.commit()