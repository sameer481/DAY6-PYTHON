"""
Day 6: Python Sets & Dictionaries Masterclass
Script 01: Dictionary Basics, Key Hashability & Core Operations

This script covers:
- Dictionary creation methods (literals, dict(), dict.fromkeys(), zip)
- Key hashability rules (immutable vs mutable keys)
- Accessing dictionary elements ([] vs .get())
- Modifying, inserting, and deleting key-value pairs
- Checking membership, length, and dictionary equality
"""

import sys
import io

# Ensure UTF-8 stdout encoding for Windows compatibility
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def section(title: str):
    """Utility helper for printing formatted section headers."""
    print(f"\n{'=' * 70}")
    print(f" [SECTION] {title}")
    print(f"{'=' * 70}")


def main():
    # ---------------------------------------------------------
    # SECTION 1: Dictionary Creation Methods
    # ---------------------------------------------------------
    section("1. DICTIONARY CREATION METHODS")

    # 1. Curly brace literal syntax {}
    user_profile = {
        "user_id": 1001,
        "username": "alex_dev",
        "email": "alex@example.com",
        "is_active": True,
        "skills": ["Python", "SQL", "Git"]
    }
    print("1. Dict literal syntax:", user_profile)
    print("   Type:", type(user_profile))

    # 2. dict() constructor with keyword arguments
    server_config = dict(host="localhost", port=8080, debug=True)
    print("2. dict() constructor with kwargs:", server_config)

    # 3. dict() with list of key-value tuples
    pairs = [("ID", 42), ("Name", "Data Science Core"), ("Duration_Weeks", 12)]
    course_info = dict(pairs)
    print("3. dict() from tuple pairs:", course_info)

    # 4. dict.fromkeys() - initializing default values
    headers = ["Content-Type", "Authorization", "Accept", "User-Agent"]
    default_headers = dict.fromkeys(headers, "application/json")
    print("4. dict.fromkeys():", default_headers)

    # 5. Zipping two lists into a dictionary
    keys = ["apple", "banana", "cherry"]
    prices = [1.20, 0.50, 2.50]
    fruit_prices = dict(zip(keys, prices))
    print("5. dict(zip(keys, values)):", fruit_prices)

    # ---------------------------------------------------------
    # SECTION 2: Key Hashability & Constraints
    # ---------------------------------------------------------
    section("2. DICTIONARY KEY CONSTRAINTS & HASHABILITY")

    print("Rule: Dictionary keys MUST be IMMUTABLE and HASHABLE.")
    print("   Allowed keys: int, float, str, bool, tuple (with immutable items), frozenset")
    print("   Disallowed keys: list, dict, set (raises TypeError: unhashable type)\n")

    # Valid Hashable Keys
    valid_dict = {
        42: "Integer key",
        3.14159: "Float key",
        "name": "String key",
        True: "Boolean key (note: True hashes equal to 1)",
        (10, 20): "Tuple key (Coordinates)"
    }
    print("Valid Dict with mixed hashable keys:", valid_dict)

    # Demonstrating hash() built-in
    print("\nDemonstrating hash() for valid key types:")
    print(f"  hash('python') = {hash('python')}")
    print(f"  hash((1, 2, 3)) = {hash((1, 2, 3))}")

    # Invalid Unhashable Key Example
    print("\nAttempting to use a mutable List as a dictionary key:")
    try:
        invalid_dict = {[1, 2, 3]: "List Key"}
    except TypeError as e:
        print(f"  Caught Expected Error: {e}")

    # Note on Boolean / Integer Key Collision Gotcha
    gotcha_dict = {1: "One", True: "True Boolean"}
    print("\nGotcha - Boolean True vs Integer 1:")
    print("  dict {1: 'One', True: 'True Boolean'} result:", gotcha_dict)
    print("  Explanation: In Python, True == 1 and hash(True) == hash(1). The key 1 gets overwritten!")

    # ---------------------------------------------------------
    # SECTION 3: Accessing Dictionary Elements Safely
    # ---------------------------------------------------------
    section("3. ACCESSING DICTIONARY ELEMENTS SAFELY")

    student = {
        "name": "Sophia",
        "age": 21,
        "major": "Computer Science",
        "gpa": 3.85
    }

    # Direct Bracket Access []
    print("Direct bracket access student['name']:", student["name"])

    # Handling KeyError with direct bracket access
    print("\nAttempting direct access for a missing key:")
    try:
        print(student["graduation_year"])
    except KeyError as e:
        print(f"  KeyError caught! Key {e} does not exist.")

    # Safe Access using .get(key, default)
    print("\nSafe access using .get():")
    grad_year = student.get("graduation_year", "Not Specified")
    print(f"  student.get('graduation_year', 'Not Specified') => {grad_year}")

    gpa = student.get("gpa", 0.0)
    print(f"  student.get('gpa', 0.0) => {gpa}")

    # ---------------------------------------------------------
    # SECTION 4: Adding, Updating & Modifying Elements
    # ---------------------------------------------------------
    section("4. ADDING, UPDATING & MODIFYING ELEMENTS")

    inventory = {"laptop": 15, "mouse": 50, "keyboard": 30}
    print("Initial Inventory:", inventory)
    print(f"Initial object id: {id(inventory)}")

    # Adding a new key-value pair
    inventory["monitor"] = 20
    print("After adding 'monitor':", inventory)

    # Updating an existing value
    inventory["mouse"] = 65
    print("After updating 'mouse' stock to 65:", inventory)

    # Note on Mutability: Memory address remains the same!
    print(f"Object id after modifications: {id(inventory)} (Same ID -> Mutable in-place modification)")

    # Nested Dictionary Modification
    company = {
        "engineering": {"head": "Sarah", "team_size": 24},
        "design": {"head": "Michael", "team_size": 8}
    }
    print("\nNested Dictionary:", company)
    company["engineering"]["team_size"] += 2
    print("Updated Nested Team Size:", company["engineering"])

    # ---------------------------------------------------------
    # SECTION 5: Membership, Length & Dictionary Equality
    # ---------------------------------------------------------
    section("5. MEMBERSHIP, LENGTH & EQUALITY")

    car = {
        "brand": "Tesla",
        "model": "Model 3",
        "year": 2023,
        "color": "Midnight Silver"
    }

    # Checking key membership with 'in' and 'not in'
    print("Is 'model' in car?", "model" in car)
    print("Is 'price' in car?", "price" in car)
    print("Is 'Tesla' in car? (Checks keys, not values!)", "Tesla" in car)
    print("Is 'Tesla' in car.values()?", "Tesla" in car.values())

    # Dictionary length
    print(f"\nNumber of key-value pairs len(car): {len(car)}")

    # Dictionary Equality (Order independent in value comparison)
    dict_a = {"x": 10, "y": 20}
    dict_b = {"y": 20, "x": 10}
    print(f"\ndict_a = {dict_a}")
    print(f"dict_b = {dict_b}")
    print("dict_a == dict_b:", dict_a == dict_b)  # True
    print("dict_a is dict_b:", dict_a is dict_b)  # False (different objects in memory)


if __name__ == "__main__":
    main()
