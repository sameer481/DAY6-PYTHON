"""
Day 6: Python Sets & Dictionaries Masterclass
Script 04: Set Basics, Elements Hashability & Built-in Methods

This script covers:
- Set creation, automatic deduplication, and the empty set gotcha
- Element hashability constraints
- Adding, updating, and removing set elements (.add, .update, .remove vs .discard, .pop)
- Membership testing & iteration
- Immutable sets using frozenset
"""

import sys

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
    # SECTION 1: Set Creation & Fundamental Properties
    # ---------------------------------------------------------
    section("1. SET CREATION & FUNDAMENTAL PROPERTIES")

    # Sets are UNORDERED collections of UNIQUE, HASHABLE elements.

    # 1. Set Literal Syntax {}
    numbers_set = {10, 20, 30, 40, 50}
    print("1. Set literal syntax {}:", numbers_set)
    print("   Type:", type(numbers_set))

    # 2. Automatic Deduplication
    duplicate_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
    unique_set = set(duplicate_list)
    print("\n2. Original List with duplicates:", duplicate_list)
    print("   set(duplicate_list) deduplicated:", unique_set)

    # 3. CRITICAL GOTCHA: Empty Set Creation
    empty_dict_attempt = {}
    true_empty_set = set()
    print("\n3. Empty Set Creation Gotcha:")
    print("   type({}) =>", type(empty_dict_attempt), "(Notice {} creates a DICT!)")
    print("   type(set()) =>", type(true_empty_set), "(Correct way to create an empty set)")

    # 4. Sets are Unindexed
    print("\n4. Attempting to index a set (numbers_set[0]):")
    try:
        print(numbers_set[0])
    except TypeError as e:
        print(f"   ❌ Caught Expected Error: {e} (Sets do not support indexing or slicing)")

    # ---------------------------------------------------------
    # SECTION 2: Element Constraints & Hashability
    # ---------------------------------------------------------
    section("2. ELEMENT CONSTRAINTS & HASHABILITY")

    print("🔑 Rule: Every element inside a Set MUST be IMMUTABLE & HASHABLE.")
    print("   Valid elements: int, float, str, bool, tuple, frozenset")
    print("   Invalid elements: list, dict, set\n")

    # Valid set with tuples and primitive types
    valid_set = {1, "Python", (10, 20), True}
    print("Valid Set with tuple and primitives:", valid_set)

    # Invalid set creation attempt
    print("\nAttempting to store a mutable List inside a Set:")
    try:
        invalid_set = {1, 2, [3, 4]}
    except TypeError as e:
        print(f"   ❌ Caught Expected Error: {e}")

    # ---------------------------------------------------------
    # SECTION 3: Modifying Sets (Adding & Removing Elements)
    # ---------------------------------------------------------
    section("3. MODIFYING SETS (ADD, UPDATE, REMOVE, DISCARD, POP)")

    fruits = {"apple", "banana"}
    print("Initial fruits set:", fruits)

    # 1. add(element) - Adds a single element
    fruits.add("cherry")
    print("After .add('cherry'):", fruits)
    fruits.add("apple")  # Adding existing element has no effect
    print("After re-adding 'apple' (No change):", fruits)

    # 2. update(*iterables) - Merges elements from multiple iterables (lists, tuples, sets, strings)
    fruits.update(["date", "elderberry"], ("fig", "grape"))
    print("\nAfter .update(['date', 'elderberry'], ('fig', 'grape')):", fruits)

    # 3. remove(element) vs discard(element)
    print("\nRemoval Comparison:")
    fruits.remove("date")
    print("  After .remove('date'):", fruits)

    print("  Attempting .remove('missing_fruit'):")
    try:
        fruits.remove("missing_fruit")
    except KeyError as e:
        print(f"    ❌ KeyError caught! .remove() raises KeyError for missing items.")

    fruits.discard("missing_fruit")
    print("  After .discard('missing_fruit'): No error raised! (.discard is safe)")

    # 4. pop() - Removes and returns an ARBITRARY element
    popped_item = fruits.pop()
    print(f"\nAfter .pop(): Removed arbitrary item '{popped_item}', Set: {fruits}")

    # 5. clear() - Empties the set
    temp_set = {1, 2, 3}
    temp_set.clear()
    print("After .clear():", temp_set)

    # ---------------------------------------------------------
    # SECTION 4: Membership Testing & Iteration
    # ---------------------------------------------------------
    section("4. MEMBERSHIP TESTING & ITERATION")

    tech_stack = {"Python", "Docker", "Kubernetes", "PostgreSQL", "Redis"}

    # Membership test is O(1) constant time complexity for Sets!
    print("Is 'Python' in tech_stack?", "Python" in tech_stack)
    print("Is 'Java' in tech_stack?", "Java" in tech_stack)

    print("\nIterating through tech_stack:")
    for tech in tech_stack:
        print(f"  - {tech}")

    # ---------------------------------------------------------
    # SECTION 5: Immutable Sets with frozenset
    # ---------------------------------------------------------
    section("5. IMMUTABLE SETS: frozenset")

    # frozenset is an immutable, hashable version of set.
    # Elements cannot be added or removed after creation.

    fs1 = frozenset([10, 20, 30, 40])
    fs2 = frozenset([30, 40, 50, 60])

    print("frozenset fs1:", fs1)
    print("frozenset fs2:", fs2)
    print("Type:", type(fs1))

    # Attempting modification raises AttributeError
    print("\nAttempting to call .add() on frozenset:")
    try:
        fs1.add(50)
    except AttributeError as e:
        print(f"   ❌ Caught Expected Error: {e}")

    # frozenset can be used as a Dictionary Key or a Set Element!
    group_permissions = {
        frozenset(["read", "write"]): "Editor Role",
        frozenset(["read", "write", "execute"]): "Admin Role"
    }

    query = frozenset(["read", "write"])
    print("\nUsing frozenset as dict key lookup:", group_permissions[query])


if __name__ == "__main__":
    main()
