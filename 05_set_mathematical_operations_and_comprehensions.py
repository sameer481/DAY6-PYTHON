"""
Day 6: Python Sets & Dictionaries Masterclass
Script 05: Mathematical Set Operations, Comparisons & Performance Benchmarks

This script covers:
- Venn diagram mathematical operations: Union, Intersection, Difference, Symmetric Difference
- In-place set update methods (|=, &=, -=, ^=)
- Set subset, superset, and disjoint relationship tests
- Set Comprehensions
- High-Performance Benchmark: O(1) Set lookup vs O(n) List lookup
"""

import sys
import time

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
    # SECTION 1: Mathematical Set Operations
    # ---------------------------------------------------------
    section("1. MATHEMATICAL SET OPERATIONS")

    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}\n")

    # 1. UNION (A | B or A.union(B)) - Combined unique elements
    union_op = set_a | set_b
    union_method = set_a.union(set_b)
    print("1. UNION (A | B):", union_op)
    print("   Method equivalence (set_a.union(set_b)):", union_method)

    # 2. INTERSECTION (A & B or A.intersection(B)) - Elements in BOTH A and B
    intersection_op = set_a & set_b
    intersection_method = set_a.intersection(set_b)
    print("\n2. INTERSECTION (A & B):", intersection_op)

    # 3. DIFFERENCE (A - B or A.difference(B)) - Elements in A BUT NOT in B
    diff_a_b = set_a - set_b
    diff_b_a = set_b - set_a
    print("\n3. DIFFERENCE (A - B):", diff_a_b, "(In A, not B)")
    print("   DIFFERENCE (B - A):", diff_b_a, "(In B, not A)")

    # 4. SYMMETRIC DIFFERENCE (A ^ B or A.symmetric_difference(B)) - Elements in A OR B, but NOT BOTH
    sym_diff = set_a ^ set_b
    print("\n4. SYMMETRIC DIFFERENCE (A ^ B):", sym_diff)

    # In-place Update Operations
    print("\n[In-Place Modifications]")
    temp_set = set_a.copy()
    temp_set &= set_b  # Keeps only common elements
    print("temp_set &= set_b (In-place Intersection):", temp_set)

    temp_set = set_a.copy()
    temp_set -= set_b  # Removes elements present in set_b
    print("temp_set -= set_b (In-place Difference):", temp_set)

    # ---------------------------------------------------------
    # SECTION 2: Set Comparisons & Relationships
    # ---------------------------------------------------------
    section("2. SET COMPARISONS & RELATIONSHIP TESTS")

    s1 = {1, 2, 3}
    s2 = {1, 2, 3, 4, 5}
    s3 = {10, 20, 30}

    print(f"s1 = {s1}")
    print(f"s2 = {s2}")
    print(f"s3 = {s3}\n")

    # 1. SUBSET (<= or .issubset())
    print("1. Subsets:")
    print("   Is s1 <= s2 (Subset)?", s1 <= s2)
    print("   s1.issubset(s2):     ", s1.issubset(s2))
    print("   Is s1 < s2 (Proper Subset)?", s1 < s2, "(Proper subset requires s1 != s2)")
    print("   Is s1 <= s1?", s1 <= s1)
    print("   Is s1 < s1 (Proper)?", s1 < s1)

    # 2. SUPERSET (>= or .issuperset())
    print("\n2. Supersets:")
    print("   Is s2 >= s1 (Superset)?", s2 >= s1)
    print("   s2.issuperset(s1):     ", s2.issuperset(s1))
    print("   Is s2 > s1 (Proper Superset)?", s2 > s1)

    # 3. DISJOINT (.isdisjoint()) - No elements in common
    print("\n3. Disjoint Sets:")
    print("   s1.isdisjoint(s2)?", s1.isdisjoint(s2))  # False (shares 1, 2, 3)
    print("   s1.isdisjoint(s3)?", s1.isdisjoint(s3))  # True (no shared elements)

    # ---------------------------------------------------------
    # SECTION 3: Set Comprehensions
    # ---------------------------------------------------------
    section("3. SET COMPREHENSIONS")

    # Syntax: {expr for item in iterable if condition}
    words = ["APPLE", "banana", "Cherry", "DATE", "fig", "banana", "APPLE"]

    # Deduplicate and convert to lowercase
    clean_words = {word.lower() for word in words}
    print("1. Lowercased deduplicated set:", clean_words)

    # Filter vowels from string
    text = "The quick brown fox jumps over the lazy dog"
    unique_vowels = {char for char in text.lower() if char in "aeiou"}
    print(f"2. Unique vowels in text:", unique_vowels)

    # Even squares set
    even_squares_set = {x**2 for x in range(1, 15) if x % 2 == 0}
    print("3. Even squares set:", even_squares_set)

    # ---------------------------------------------------------
    # SECTION 4: High-Performance Lookup Benchmark (Set vs List)
    # ---------------------------------------------------------
    section("4. PERFORMANCE BENCHMARK: O(1) SET VS O(n) LIST LOOKUP")

    # Generate 1 million elements
    N = 1_000_000
    print(f"Generating data structures with {N:,} elements...")

    data_list = list(range(N))
    data_set = set(data_list)

    target_element = 999_999  # Worst-case search target (at the very end of list)
    num_iterations = 100

    print(f"Performing {num_iterations} lookup iterations for item {target_element:,}...\n")

    # Benchmark List Lookup - O(n) Linear Time
    start_time = time.perf_counter()
    for _ in range(num_iterations):
        _ = target_element in data_list
    list_duration = (time.perf_counter() - start_time) * 1000

    # Benchmark Set Lookup - O(1) Constant Time (Hash Table)
    start_time = time.perf_counter()
    for _ in range(num_iterations):
        _ = target_element in data_set
    set_duration = (time.perf_counter() - start_time) * 1000

    print(f"⏱️ List Lookup Total Time ({num_iterations} ops): {list_duration:.4f} ms")
    print(f"⏱️ Set Lookup Total Time  ({num_iterations} ops): {set_duration:.4f} ms")

    if set_duration > 0:
        speedup = list_duration / set_duration
        print(f"\n🚀 RESULT: Set lookup is approximately {speedup:,.1f}x FASTER than List lookup!")
    print("💡 Takeaway: Always convert large collections to a Set when doing frequent membership checks ('in' operator)!")


if __name__ == "__main__":
    main()
