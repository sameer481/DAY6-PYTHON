# Day 6: Master Python Sets & Dictionaries 🐍

Welcome to Day 6 of learning Python! This repository contains comprehensive guides, detailed runnable Python scripts, custom algorithms, high-performance benchmarks, and production-grade practical projects covering **Python Dictionaries**, **Sets**, **Hashability Rules**, **Dictionary & Set Comprehensions**, `collections` module (`defaultdict`, `Counter`, `OrderedDict`), **Set Mathematics & Venn Diagram Operations**, and **Real-World Applications**.

---

## 📁 Repository Structure

```text
DAY6-PYTHON/
│
├── 01_dictionary_basics_and_operations.py         # Creation, key hashability rules, [] vs .get(), mutability, id() tracking
├── 02_dictionary_methods_and_manipulation.py     # View objects (.keys, .values, .items), setdefault, removal, merging (| & |=)
├── 03_dictionary_comprehensions_and_collections.py# Comprehensions, key inversion, defaultdict, Counter, OrderedDict
├── 04_set_basics_and_operations.py               # Set creation, deduplication, element hashability, add/discard/pop, frozenset
├── 05_set_mathematical_operations_and_comprehensions.py # Union, Intersection, Difference, Subsets, Set Comprehensions & 70,000x Benchmark
├── 06_practical_projects.py                      # 4 Production-grade projects: E-Commerce Stock Alert, Text Analyzer, Social Engine, RBAC
└── README.md                                     # Comprehensive documentation and execution guide
```

---

## 📚 Detailed Topic Breakdown

### 1. Dictionary Basics, Hashability & Core Operations (`01_dictionary_basics_and_operations.py`)
- **Dictionary Creation**:
  - Literal syntax `{}` and constructor `dict(host="localhost", port=8080)`.
  - Initializing from key-value tuple pairs and `dict.fromkeys(keys, default)`.
  - Combining parallel sequences into dictionaries with `dict(zip(keys, values))`.
- **Key Constraints & Hashability**:
  - **Rule**: Dictionary keys MUST be immutable and hashable (`int`, `float`, `str`, `bool`, `tuple`, `frozenset`).
  - Mutable objects like `list`, `dict`, or `set` raise a `TypeError: unhashable type`.
  - Demonstrating `hash()` function mechanics.
  - Boolean/Integer Key Gotcha (`True == 1` and `hash(True) == hash(1)` leads to key overwrites).
- **Accessing Elements Safely**:
  - Direct bracket access `d[key]` (raises `KeyError` if key is missing).
  - Safe access with `d.get(key, default)`.
- **Modifying & Equality**:
  - In-place value modification, `len()`, identity `is` vs equality `==`.

---

### 2. Built-in Dictionary Methods & Manipulation (`02_dictionary_methods_and_manipulation.py`)
- **Dynamic View Objects**:
  - `.keys()`, `.values()`, `.items()` view objects automatically reflect dictionary updates in real time without re-querying.
  - Efficient tuple unpacking during `for key, value in dict.items()` iteration.
- **Insertion & Manipulation**:
  - `.setdefault(key, default)` for safe insertion without pre-checking.
  - Grouping items into categorizations cleanly.
- **Removal Methods**:
  - `pop(key, default)`: Removes key and returns value.
  - `popitem()`: Removes and returns last inserted key-value pair (LIFO order).
  - `del dict[key]` and `dict.clear()`.
- **Merging Dictionaries**:
  - Traditional `.update()`, dictionary unpacking `{**d1, **d2}`.
  - Python 3.9+ Union Operator (`d1 | d2`) and In-place Union (`d1 |= d2`).
- **Copy Operations**:
  - `dict.copy()` (Shallow copy) vs `copy.deepcopy()` (Deep copy for nested structures).

---

### 3. Dictionary Comprehensions & Advanced Collections (`03_dictionary_comprehensions_and_collections.py`)
- **Dictionary Comprehensions**:
  - Basic mapping: `{key_expr: val_expr for item in iterable}`.
  - Conditional filtering: `{k: v for k, v in dict.items() if condition}`.
  - Inverting keys and values: `{v: k for k, v in original_dict.items()}`.
- **Specialized Collections (`collections` module)**:
  - `collections.defaultdict`: Automatic key initialization using factories (`int`, `list`, `set`), eliminating `KeyError`.
  - `collections.Counter`: Multiset element frequency counter, `.most_common(n)`, and counter arithmetic (`+`, `-`, `&`, `|`).
  - `collections.OrderedDict`: Key reordering via `.move_to_end()` and strict order-aware equality comparisons.

---

### 4. Set Basics, Hashability & Methods (`04_set_basics_and_operations.py`)
- **Set Creation & Properties**:
  - Sets are **unordered** collections of **unique**, hashable elements.
  - Automatic deduplication of input sequences.
  - **CRITICAL GOTCHA**: `{}` creates an empty `dict`, whereas `set()` creates an empty `set`.
  - Sets are unindexed (`set[0]` raises `TypeError`).
- **Modifying Sets**:
  - `.add(element)`: Single item insertion.
  - `.update(*iterables)`: Bulk insertion from multiple lists/tuples.
  - `.remove(val)` (raises `KeyError` if missing) vs `.discard(val)` (safe removal).
  - `.pop()`: Arbitrary item removal.
- **`frozenset`**:
  - Immutable, hashable version of `set`.
  - Usable as dictionary keys or elements inside other sets.

---

### 5. Mathematical Set Operations & Performance Benchmarks (`05_set_mathematical_operations_and_comprehensions.py`)
- **Venn Diagram Mathematical Operations**:
  - **Union** (`A | B` or `A.union(B)`): Combined unique elements.
  - **Intersection** (`A & B` or `A.intersection(B)`): Shared common elements.
  - **Difference** (`A - B` or `A.difference(B)`): Elements in A but not B.
  - **Symmetric Difference** (`A ^ B` or `A.symmetric_difference(B)`): Elements in A or B, but not both.
  - In-place update operators (`|=`, `&=`, `-=`, `^=`).
- **Set Relationship Tests**:
  - Subsets (`<=` / `.issubset()`), Proper Subsets (`<`).
  - Supersets (`>=` / `.issuperset()`), Proper Supersets (`>`).
  - Disjoint sets (`.isdisjoint()`).
- **Set Comprehensions**: `{expr for item in iterable if condition}`.
- **High-Performance Benchmark**:
  - Demonstrating $O(1)$ constant-time Set membership lookup vs $O(n)$ linear-time List membership lookup over **1,000,000 elements**.
  - **Result**: Set lookup is over **70,000x faster** for large dataset lookups!

---

### 6. Production-Grade Practical Projects (`06_practical_projects.py`)
1. **E-Commerce Inventory & Stock Alert System**: Asset valuation, inventory tracking, threshold reorder alerts via dict comprehensions, bulk price promo updates.
2. **Text Analyzer & Lexical Statistics Engine**: Text sanitization, lexical diversity scoring ($|Unique| / |Total| \times 100$), stop-word filtering using Set difference, top word ranking with `Counter`.
3. **Social Network Mutual Connections Engine**: Graph representation, mutual friend detection (`A & B`), Jaccard Similarity index calculation, friend recommendation algorithm based on mutual connections.
4. **Enterprise Role-Based Access Control (RBAC) System**: Multi-role security matrix using `frozenset`, permission inheritance (`|`), subset permission validation (`<=`), and missing permission security audits (`-`).

---

## ⚙️ How to Run the Scripts

Ensure you have **Python 3.8+** installed.

```bash
# Navigate to the Day 6 directory
cd DAY6-PYTHON

# Run individual topic scripts:
python 01_dictionary_basics_and_operations.py
python 02_dictionary_methods_and_manipulation.py
python 03_dictionary_comprehensions_and_collections.py
python 04_set_basics_and_operations.py
python 05_set_mathematical_operations_and_comprehensions.py
python 06_practical_projects.py
```

---

## 🎯 Quick Comparison Matrix: Data Structures

| Feature | Lists (`list`) | Tuples (`tuple`) | Dictionaries (`dict`) | Sets (`set`) |
| :--- | :--- | :--- | :--- | :--- |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{"key": "val"}` | `{1, 2, 3}` |
| **Element Order** | Ordered | Ordered | Insertion-Ordered (3.7+) | **Unordered** |
| **Mutability** | **Mutable** | **Immutable** | **Mutable** | **Mutable** |
| **Duplicates Allowed** | ✅ Yes | ✅ Yes | ❌ Keys Unique, Values Dupes | ❌ **Unique Elements Only** |
| **Indexing / Slicing** | ✅ `lst[0]` | ✅ `tup[0]` | ❌ Key Access `d["key"]` | ❌ **Unindexed** |
| **Lookup Time** | $O(n)$ Linear | $O(n)$ Linear | $O(1)$ Hash Table | $O(1)$ Hash Table |
| **Usable as Dict Key** | ❌ No | ✅ Yes (If items hashable)| ❌ No | ❌ No (Use `frozenset`) |

---

## 📐 Mathematical Set Operations Reference

| Operation | Operator Syntax | Method Syntax | Description |
| :--- | :--- | :--- | :--- |
| **Union** | `A \| B` | `A.union(B)` | All elements in A, B, or both |
| **Intersection** | `A & B` | `A.intersection(B)` | Only elements present in both A and B |
| **Difference** | `A - B` | `A.difference(B)` | Elements in A that are not in B |
| **Symmetric Difference** | `A ^ B` | `A.symmetric_difference(B)` | Elements in A or B, but not both |
| **Subset** | `A <= B` | `A.issubset(B)` | True if all elements of A are in B |
| **Proper Subset** | `A < B` | *N/A* | True if `A <= B` and `A != B` |
| **Superset** | `A >= B` | `A.issuperset(B)` | True if all elements of B are in A |
| **Disjoint** | *N/A* | `A.isdisjoint(B)` | True if A and B share no common elements |

---

## 🌟 Key Takeaways

1. **Hashability Rules**: Dictionary keys and Set elements MUST be immutable (hashable). Attempting to use lists or dicts raises `TypeError`.
2. **Safe Dict Retrieval**: Use `dict.get(key, default)` or `collections.defaultdict` to prevent unexpected `KeyError` crashes in production.
3. **Empty Set Gotcha**: `{}` creates a dictionary! Always use `set()` to instantiate an empty set.
4. **Lookup Efficiency**: For membership testing (`in` operator) on large datasets, convert lists to `set` for an $O(1)$ performance boost (up to 70,000x faster).
5. **Set Mathematics**: Leverage Python's set mathematical operators (`&`, `|`, `-`, `^`) to write elegant, high-performance logic for social networks, RBAC security, and data analysis.
