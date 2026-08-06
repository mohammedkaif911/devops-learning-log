total_venue = 0
max_sale = 0
top_product = ""
try:
    with open ("sales.csv","r") as f:
        for lines in f:
            if lines.lower().startswith("product"):
                continue
            parts = lines.strip().split(",")
            product = parts[0]
            units = int(parts[1])
            perunit_price = float(parts[2])
            revenue = units * perunit_price
            total_venue +=revenue
            if revenue > max_sale:
                max_sale = revenue
                top_product = product
    print(f"Total revenue = ${total_venue:.2f}")
    print(f"Top product = {top_product} with value ${max_sale:.2f}")
except FileNotFoundError:
    print("[ERROR] Database file 'sales.csv' is missing!")
    
