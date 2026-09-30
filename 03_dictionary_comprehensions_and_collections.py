"""
Day 6: Python Sets & Dictionaries Masterclass
Script 03: Dictionary Comprehensions & Advanced Collections

This script covers:
- Dictionary Comprehension syntax and conditional expressions
- Practical dictionary transform techniques (inverting, filtering)
- Specialized dict structures: collections.defaultdict
- Frequency counting with collections.Counter
- Reordering and LRU cache structures with collections.OrderedDict
"""

import sys
from collections import defaultdict, Counter, OrderedDict

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
    # SECTION 1: Dictionary Comprehensions Syntax & Filtering
    # ---------------------------------------------------------
    section("1. DICTIONARY COMPREHENSIONS & FILTERING")

    # Syntax: {key_expr: val_expr for item in iterable}
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Map number -> square
    squares = {x: x**2 for x in numbers}
    print("1. Squares dict {x: x**2}:", squares)

    # Filtered Comprehension (with 'if' condition)
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    print("2. Even Squares {x: x**2 for x in numbers if x % 2 == 0}:", even_squares)

    # Ternary Mapping (with 'if-else' expression)
    odd_even_map = {x: "EVEN" if x % 2 == 0 else "ODD" for x in numbers}
    print("3. Odd/Even Map:", odd_even_map)

    # ---------------------------------------------------------
    # SECTION 2: Advanced Dict Comprehension Transformations
    # ---------------------------------------------------------
    section("2. ADVANCED DICT COMPREHENSION TRANSFORMATIONS")

    # A. Inverting Keys & Values {val: key for key, val in dict.items()}
    original_ports = {"HTTP": 80, "HTTPS": 443, "FTP": 21, "SSH": 22}
    inverted_ports = {port: protocol for protocol, port in original_ports.items()}
    print("Original Port Map: ", original_ports)
    print("Inverted Port Map: ", inverted_ports)

    # B. Filtering & Transforming String Heights (Imperial to Metric conversion)
    city_temperatures_f = {"New York": 75, "London": 59, "Tokyo": 82, "Sydney": 68}
    # Conversion formula: (F - 32) * 5/9
    city_temperatures_c = {
        city: round((temp - 32) * 5 / 9, 1)
        for city, temp in city_temperatures_f.items()
        if temp >= 60
    }
    print("\nWarm Cities (Temp >= 60°F converted to °C):", city_temperatures_c)

    # C. Character Frequency with dict comprehension & str.count
    sample_str = "abracadabra"
    char_freq = {char: sample_str.count(char) for char in set(sample_str)}
    print(f"\nCharacter Frequencies in '{sample_str}':", char_freq)

    # ---------------------------------------------------------
    # SECTION 3: collections.defaultdict
    # ---------------------------------------------------------
    section("3. SPECIALIZED DICT: collections.defaultdict")

    # defaultdict automatically initializes missing keys using a factory function (int, list, set, etc.)

    # 1. defaultdict(int) - Automatic counter
    print("1. defaultdict(int) - Letter Counter:")
    word_counter = defaultdict(int)
    for char in "mississippi":
        word_counter[char] += 1  # No KeyError! Default for missing key is 0
    print("   Result:", dict(word_counter))

    # 2. defaultdict(list) - Grouping items
    print("\n2. defaultdict(list) - Grouping Words by Length:")
    words = ["apple", "bat", "car", "elephant", "dog", "banana"]
    grouped_by_length = defaultdict(list)
    for word in words:
        grouped_by_length[len(word)].append(word)

    for length, word_list in sorted(grouped_by_length.items()):
        print(f"   Length {length}: {word_list}")

    # 3. defaultdict(set) - Grouping Unique Values
    print("\n3. defaultdict(set) - User Action Collector:")
    user_actions = [("user1", "login"), ("user2", "click"), ("user1", "purchase"), ("user1", "login")]
    user_activity_map = defaultdict(set)
    for user, action in user_actions:
        user_activity_map[user].add(action)
    print("   Unique User Actions:", dict(user_activity_map))

    # ---------------------------------------------------------
    # SECTION 4: collections.Counter
    # ---------------------------------------------------------
    section("4. FREQUENCY COUNTING WITH collections.Counter")

    # Counter is a dict subclass for counting hashable objects
    items = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]
    counts = Counter(items)

    print("Counter object:", counts)
    print("Most common 2 items (.most_common(2)):", counts.most_common(2))
    print("Count of 'apple':", counts["apple"])
    print("Count of missing 'mango':", counts["mango"])  # Returns 0 instead of KeyError!

    # Arithmetic Operations on Counters
    c1 = Counter(a=3, b=1, c=4)
    c2 = Counter(a=1, b=2, c=1)
    print("\nc1:", c1)
    print("c2:", c2)
    print("c1 + c2 (Combined counts):", c1 + c2)
    print("c1 - c2 (Subtracted counts):", c1 - c2)
    print("c1 & c2 (Min counts / Intersection):", c1 & c2)
    print("c1 | c2 (Max counts / Union):", c1 | c2)

    # ---------------------------------------------------------
    # SECTION 5: collections.OrderedDict
    # ---------------------------------------------------------
    section("5. ORDER PRESERVATION & collections.OrderedDict")

    # Note: Since Python 3.7, standard dicts preserve insertion order.
    # However, OrderedDict provides order-specific capabilities:
    # 1. move_to_end(key, last=True/False)
    # 2. Equality comparison takes order into account!

    od1 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    od2 = OrderedDict([("b", 2), ("a", 1), ("c", 3)])
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"b": 2, "a": 1, "c": 3}

    print("Standard dict equality (d1 == d2):", d1 == d2)       # True (ignores order)
    print("OrderedDict equality (od1 == od2):", od1 == od2)   # False (considers order!)

    # Reordering keys with move_to_end()
    print("\nOriginal OrderedDict od1:", od1)
    od1.move_to_end("a", last=True)
    print("After move_to_end('a', last=True):", od1)
    od1.move_to_end("c", last=False)
    print("After move_to_end('c', last=False):", od1)


if __name__ == "__main__":
    main()
