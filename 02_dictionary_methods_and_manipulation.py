"""
Day 6: Python Sets & Dictionaries Masterclass
Script 02: Built-in Dictionary Methods & Manipulation

This script covers:
- Dictionary View Objects (.keys(), .values(), .items()) and their dynamic behavior
- Insertion/Modification helper methods (.setdefault(), .update())
- Removal techniques (pop(), popitem(), del, clear())
- Merging Dictionaries (update, **unpacking, | operator, |= operator)
- Shallow Copy (.copy()) vs Deep Copy (copy.deepcopy())
"""

import sys
import copy

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
    # SECTION 1: Dictionary View Objects & Dynamic Behavior
    # ---------------------------------------------------------
    section("1. DICTIONARY VIEW OBJECTS & DYNAMIC BEHAVIOR")

    scores = {"Alice": 95, "Bob": 88, "Charlie": 92}

    # Extracting views
    keys_view = scores.keys()
    values_view = scores.values()
    items_view = scores.items()

    print("keys_view:", keys_view, "| Type:", type(keys_view))
    print("values_view:", values_view, "| Type:", type(values_view))
    print("items_view:", items_view, "| Type:", type(items_view))

    # Dynamic nature: View objects automatically reflect changes made to the dictionary!
    print("\n[Dynamic Behavior Test]")
    print("Initial items view:", list(items_view))
    print("Adding 'Diana': 97 to dictionary...")
    scores["Diana"] = 97
    print("Items view after update (Without re-querying!):", list(items_view))

    # Iterating over items()
    print("\nIterating over key-value pairs with tuple unpacking:")
    for name, score in scores.items():
        print(f"  Student: {name:<10} | Score: {score}")

    # ---------------------------------------------------------
    # SECTION 2: Advanced Insertion Methods (.setdefault & .update)
    # ---------------------------------------------------------
    section("2. ADVANCED INSERTION (.setdefault & .update)")

    settings = {"theme": "dark", "font_size": 14}
    print("Initial settings:", settings)

    # setdefault(key, default_value)
    # If key exists, returns existing value. If missing, inserts key with default_value.
    theme = settings.setdefault("theme", "light")
    print(f".setdefault('theme', 'light') returns: '{theme}' (Key existed, un-modified)")

    language = settings.setdefault("language", "English")
    print(f".setdefault('language', 'English') returns: '{language}' (Key was added!)")
    print("Updated settings:", settings)

    # Grouping using setdefault
    print("\nGrouping items into a list of categories using setdefault:")
    products = [
        ("Electronics", "Laptop"),
        ("Clothing", "Jacket"),
        ("Electronics", "Smartphone"),
        ("Clothing", "Shirt"),
        ("Books", "Python Crash Course")
    ]

    categorized = {}
    for category, product in products:
        categorized.setdefault(category, []).append(product)

    for cat, items in categorized.items():
        print(f"  {cat:<15}: {items}")

    # ---------------------------------------------------------
    # SECTION 3: Removal & Deletion Methods
    # ---------------------------------------------------------
    section("3. REMOVAL & DELETION METHODS")

    app_state = {
        "user_id": 404,
        "session_token": "abc123xyz",
        "cache_expiry": 3600,
        "temp_data": "scratch",
        "debug_mode": True
    }
    print("Initial App State:", app_state)

    # 1. pop(key, default) - Removes key and returns value
    token = app_state.pop("session_token", None)
    print(f"\n1. pop('session_token') => {token}")

    missing_pop = app_state.pop("invalid_key", "Default Fallback")
    print(f"   pop('invalid_key', default) => {missing_pop}")

    # 2. popitem() - Removes and returns last inserted key-value pair as a tuple (LIFO order)
    last_item = app_state.popitem()
    print(f"\n2. popitem() => {last_item}")
    print("   State after popitem():", app_state)

    # 3. del statement - Deletes specific key or entire variable
    del app_state["temp_data"]
    print("\n3. del app_state['temp_data'] =>", app_state)

    # 4. clear() - Removes all elements, keeping dict object empty
    app_state.clear()
    print("\n4. clear() => app_state is now:", app_state)

    # ---------------------------------------------------------
    # SECTION 4: Merging Dictionaries (Python 3.9+ Features)
    # ---------------------------------------------------------
    section("4. MERGING DICTIONARIES")

    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"c": 99, "d": 4, "e": 5}

    print(f"dict1 = {dict1}")
    print(f"dict2 = {dict2}")

    # Method A: Traditional .update() (In-place modification of dict1)
    d_temp = dict1.copy()
    d_temp.update(dict2)
    print("\nMethod A (.update()):", d_temp)

    # Method B: Dictionary Unpacking ** (Returns new dictionary)
    d_unpacked = {**dict1, **dict2}
    print("Method B ({**d1, **d2}):", d_unpacked)

    # Method C: Union Operator | (Python 3.9+)
    d_union = dict1 | dict2
    print("Method C (dict1 | dict2):", d_union)

    # Method D: In-place Union Operator |= (Python 3.9+)
    d_inplace = dict1.copy()
    d_inplace |= dict2
    print("Method D (d1 |= d2):", d_inplace)

    # ---------------------------------------------------------
    # SECTION 5: Shallow Copy vs Deep Copy
    # ---------------------------------------------------------
    section("5. SHALLOW COPY VS DEEP COPY IN DICTIONARIES")

    original = {
        "title": "Data Pipeline",
        "settings": {"retry": 3, "timeout": 30}
    }

    # Shallow copy using .copy()
    shallow = original.copy()

    # Deep copy using copy.deepcopy()
    deep = copy.deepcopy(original)

    print("Original:", original)
    print("Modifying nested 'settings' -> 'timeout' = 60 in Shallow copy...")
    shallow["settings"]["timeout"] = 60

    print("\n[Result after modifying Shallow Copy]")
    print("  Original settings:", original["settings"])  # Modified! (Shared reference)
    print("  Shallow settings: ", shallow["settings"])
    print("  Deep settings:    ", deep["settings"])     # Unaffected! (Independent object)


if __name__ == "__main__":
    main()
