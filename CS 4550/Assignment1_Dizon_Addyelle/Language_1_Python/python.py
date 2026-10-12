import os
import sys
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.join(BASE_DIR, "input", "transactions.csv")
if not os.path.exists(CSV_PATH):
    parent_input_csv = os.path.join(os.path.dirname(BASE_DIR), "input", "transactions.csv")
    if os.path.exists(parent_input_csv):
        CSV_PATH = parent_input_csv

REPORT_PATH = os.path.join(BASE_DIR, "report.txt")
ERRORS_PATH = os.path.join(BASE_DIR, "errors.txt")

def trim(s):
    return s.strip()

def validate_price_format(price_str):
    if '.' in price_str:
        return len(price_str.split('.')[1]) <= 2
    return True

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: transactions.csv not found at {CSV_PATH}")
        sys.exit(1)

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != "transaction_id,product_name,category,quantity,unit_price":
        if lines:
            print("Error: Fatal header error. Incorrect or missing header.")
        else:
            write_zero_results()
        sys.exit(1)

    valid_records = []
    invalid_records = []
    seen_ids = set()

    for line_idx, line in enumerate(lines[1:], start=2):
        clean_line = line.replace('\n', '').replace('\r', '')
        fields = clean_line.split(',')
        
        if len(fields) != 5:
            invalid_records.append((line_idx, "Does not contain exactly 5 fields"))
            continue
            
        t_id_str, p_name, cat, qty_str, price_str = map(trim, fields)
        
        try:
            t_id = int(t_id_str)
            if t_id <= 0: raise ValueError
        except ValueError:
            invalid_records.append((line_idx, "Transaction ID must be a positive integer"))
            continue
            
        if t_id in seen_ids:
            invalid_records.append((line_idx, "Duplicate transaction ID"))
            continue
            
        if not p_name:
            invalid_records.append((line_idx, "Product name cannot be empty"))
            continue
            
        if not cat:
            invalid_records.append((line_idx, "Category cannot be empty"))
            continue
            
        try:
            qty = int(qty_str)
            if qty <= 0: raise ValueError
        except ValueError:
            invalid_records.append((line_idx, "Quantity must be a positive integer"))
            continue
            
        try:
            price = float(price_str)
            if price < 0.00 or not validate_price_format(price_str):
                raise ValueError
        except ValueError:
            invalid_records.append((line_idx, "Unit price must be >= 0.00 with max 2 decimals"))
            continue

        seen_ids.add(t_id)
        value = qty * price
        valid_records.append({
            'id': t_id, 'product': p_name, 'category': cat,
            'qty': qty, 'price': price, 'value': value
        })

    generate_reports(valid_records, invalid_records)
    handle_lookup(valid_records)

def write_zero_results():
    with open(REPORT_PATH, "w") as f:
        f.write("Valid transactions: 0\nInvalid transactions: 0\nTotal revenue: 0.00\nHighest-value transaction: N/A\n")
    with open(ERRORS_PATH, "w") as f:
        f.write("No invalid records\n")

def generate_reports(valid_records, invalid_records):
    total_valid = len(valid_records)
    total_invalid = len(invalid_records)
    
    if total_valid == 0:
        with open(REPORT_PATH, "w") as f:
            f.write(f"Valid transactions: 0\nInvalid transactions: {total_invalid}\nTotal revenue: 0.00\nHighest-value transaction: N/A\n")
    else:
        total_revenue = sum(r['value'] for r in valid_records)
        highest = max(valid_records, key=lambda x: (x['value'], -x['id']))
        cat_totals = defaultdict(float)
        for r in valid_records:
            cat_totals[r['category']] += r['value']
            
        sorted_records = sorted(valid_records, key=lambda x: (-x['value'], x['id']))
        
        with open(REPORT_PATH, "w") as f:
            f.write(f"Valid transactions: {total_valid}\n")
            f.write(f"Invalid transactions: {total_invalid}\n")
            f.write(f"Total revenue: {total_revenue:.2f}\n")
            f.write(f"Highest-value transaction: ID {highest['id']}, {highest['product']}, {highest['category']}, Qty {highest['qty']}, Price {highest['price']:.2f}, Value {highest['value']:.2f}\n")
            f.write("\nCategory Totals:\n")
            for cat in sorted(cat_totals.keys()):
                f.write(f"{cat}: {cat_totals[cat]:.2f}\n")
            f.write("\nSorted Transactions:\n")
            for r in sorted_records:
                f.write(f"{r['id']},{r['product']},{r['category']},{r['qty']},{r['price']:.2f},{r['value']:.2f}\n")

    with open(ERRORS_PATH, "w") as f:
        if not invalid_records:
            f.write("No invalid records\n")
        else:
            for line_idx, reason in invalid_records:
                f.write(f"Line {line_idx}: {reason}\n")

def handle_lookup(valid_records):
    if not valid_records:
        print("No valid transactions available for lookup.")
        return
        
    while True:
        try:
            lookup_input = input("Enter a positive integer Transaction ID for lookup: ").strip()
            lookup_id = int(lookup_input)
            if lookup_id <= 0:
                print("ID must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Must be a positive integer.")
            
    match = next((r for r in valid_records if r['id'] == lookup_id), None)
    if match:
        print(f"Found: ID {match['id']}, {match['product']}, {match['category']}, Qty {match['qty']}, Price {match['price']:.2f}, Value {match['value']:.2f}")
    else:
        print(f"Transaction ID {lookup_id} does not exist among valid records.")

if __name__ == "__main__":
    main()