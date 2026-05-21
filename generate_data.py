import pandas as pd
import random
from datetime import datetime, timedelta

products = [
    ("Basic White T-Shirt", "Tops", 799),
    ("Oversized Graphic Tee", "Tops", 999),
    ("Polo T-Shirt", "Tops", 1199),
    ("Slim Fit Jeans", "Bottoms", 1999),
    ("Cargo Pants", "Bottoms", 1799),
    ("Joggers", "Bottoms", 1499),
    ("Floral Kurti", "Ethnic Wear", 1599),
    ("Cotton Kurta", "Ethnic Wear", 1899),
    ("Sneakers", "Footwear", 2499),
    ("Sandals", "Footwear", 1299),
    ("Wallet", "Accessories", 599),
    ("Cap", "Accessories", 499)
]

sizes = ["XS", "S", "M", "L", "XL"]

colors = [
    "Black",
    "White",
    "Blue",
    "Red",
    "Navy Blue",
    "Grey"
]

payments = ["Cash", "UPI", "Card"]

genders = ["Male", "Female", "Other"]

age_groups = [
    "Teen",
    "Young Adult",
    "Adult",
    "Senior"
]

sections = ["Men", "Women", "Kids", "Accessories"]

rows = []

start_date = datetime(2026, 4, 1)

for i in range(200):

    date = start_date + timedelta(days=random.randint(0, 29))
    day = date.strftime("%A")

    # Weekend sales boost
    if day in ["Saturday", "Sunday"]:
        quantity = random.randint(2, 5)
    # Tuesday slow sales
    elif day == "Tuesday":
        quantity = random.randint(1, 2)
    else:
        quantity = random.randint(1, 4)

    product = random.choice(products)

    # M and L more popular
    size = random.choices(
        sizes,
        weights=[5, 15, 40, 30, 10]
    )[0]

    # Wallet intentionally slow-selling
    if product[0] == "Wallet":
        quantity = 1

    # Sneakers strong seller
    if product[0] == "Sneakers":
        quantity += 2

    discount = random.choice([0, 10, 20, 30, 50])

    price = product[2]

    total = quantity * price * (1 - discount / 100)

    row = {
        "sale_id": f"S{i+1:03}",
        "date": date.date(),
        "day_of_week": day,
        "product_name": product[0],
        "category": product[1],
        "size": size,
        "color": random.choice(colors),
        "quantity_sold": quantity,
        "price (Rs.)": price,
        "discount (%)": discount,
        "total_amount (Rs.)": round(total, 2),
        "payment_method": random.choice(payments),
        "customer_gender": random.choice(genders),
        "age_group": random.choice(age_groups),
        "store_section": random.choice(sections)
    }

    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("sales_data.csv", index=False)

print("sales_data.csv created successfully!")