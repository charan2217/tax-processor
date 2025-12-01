# tax_processor.py
import csv
import sys

def calc_tax(income):
    """
    Simple example tax bands:
    - up to 25000: 0%
    - 25001 - 50000: 10%
    - 50001 - 100000: 20%
    - above 100000: 30%
    """
    inc = float(income)
    if inc <= 25000:
        return 0.0
    elif inc <= 50000:
        return (inc - 25000) * 0.10
    elif inc <= 100000:
        return (25000 * 0.10) + (inc - 50000) * 0.20
    else:
        return (25000 * 0.10) + (50000 * 0.20) + (inc - 100000) * 0.30

def process_file(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        print(f"{'Name':30} {'Income':>10} {'Tax':>10}")
        print("-"*54)
        for row in reader:
            name = row.get("name", "")
            income = row.get("income", "0")
            tax = calc_tax(income)
            print(f"{name:30} {float(income):10.2f} {tax:10.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tax_processor.py data/sample.csv")
    else:
        process_file(sys.argv[1])
