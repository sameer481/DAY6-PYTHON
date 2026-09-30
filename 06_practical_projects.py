"""
Day 6: Python Sets & Dictionaries Masterclass
Script 06: Real-World Practical Projects

This script implements 4 production-grade projects:
1. E-Commerce Inventory & Stock Alert System
2. Text Analyzer & Lexical Statistics Engine
3. Social Network Mutual Connections & Recommendation Engine
4. Enterprise Role-Based Access Control (RBAC) Security System
"""

import sys
import re
from collections import Counter, defaultdict

# Ensure UTF-8 stdout encoding for Windows compatibility
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def section(title: str):
    """Utility helper for printing formatted section headers."""
    print(f"\n{'=' * 80}")
    print(f" 🚀 PROJECT: {title}")
    print(f"{'=' * 80}")


# =====================================================================
# PROJECT 1: E-COMMERCE INVENTORY & STOCK ALERT SYSTEM
# =====================================================================
def project_inventory_system():
    section("1. E-COMMERCE INVENTORY & STOCK MANAGEMENT SYSTEM")

    inventory = {
        "PROD-001": {"name": "Wireless Mouse", "price": 29.99, "stock": 45, "category": "Peripherals"},
        "PROD-002": {"name": "Mechanical Keyboard", "price": 89.99, "stock": 8, "category": "Peripherals"},
        "PROD-003": {"name": "27-inch 4K Monitor", "price": 349.50, "stock": 4, "category": "Displays"},
        "PROD-004": {"name": "USB-C Docking Station", "price": 119.00, "stock": 15, "category": "Accessories"},
        "PROD-005": {"name": "Noise Canceling Headphones", "price": 199.99, "stock": 2, "category": "Audio"}
    }

    # 1. Calculate Total Warehouse Asset Valuation
    total_value = sum(item["price"] * item["stock"] for item in inventory.values())
    print(f"📦 Total Warehouse Valuation: ${total_value:,.2f}")

    # 2. Identify Low Stock Items (Stock < 10 threshold) using Dict Comprehension
    REORDER_THRESHOLD = 10
    reorder_alerts = {
        code: item
        for code, item in inventory.items()
        if item["stock"] < REORDER_THRESHOLD
    }

    print(f"\n⚠️  REORDER ALERTS (Stock < {REORDER_THRESHOLD}):")
    print("-" * 65)
    print(f"{'SKU Code':<12} | {'Product Name':<28} | {'Stock':<6} | {'Price'}")
    print("-" * 65)
    for sku, details in reorder_alerts.items():
        print(f"{sku:<12} | {details['name']:<28} | {details['stock']:<6} | ${details['price']:.2f}")

    # 3. Bulk Price Discount Update (10% off Displays & Audio)
    print("\n🏷️  Applying 10% promotional discount to 'Displays' and 'Audio'...")
    for details in inventory.values():
        if details["category"] in {"Displays", "Audio"}:
            details["price"] = round(details["price"] * 0.90, 2)

    print("  Updated Monitor Price:", inventory["PROD-003"]["price"])
    print("  Updated Headphones Price:", inventory["PROD-005"]["price"])


# =====================================================================
# PROJECT 2: TEXT ANALYZER & LEXICAL STATISTICS ENGINE
# =====================================================================
def project_text_analyzer():
    section("2. TEXT ANALYZER & LEXICAL STATISTICS ENGINE")

    raw_article = """
    Python is an incredibly powerful programming language. Python is widely used in data science, 
    machine learning, web development, and automation. Machine learning models in Python leverage 
    specialized libraries like NumPy, Pandas, and PyTorch. Python programming focuses on code readability 
    and elegance. Learning Python opens vast career opportunities in technology!
    """

    # 1. Clean & tokenize text (Regex to keep words only)
    words = re.findall(r'\b[a-z0-9]+\b', raw_article.lower())
    total_words = len(words)
    unique_words_set = set(words)

    # 2. Calculate Lexical Diversity
    lexical_diversity = (len(unique_words_set) / total_words) * 100 if total_words > 0 else 0.0

    print(f"📊 Article Analysis Statistics:")
    print(f"   - Total Word Count: {total_words}")
    print(f"   - Unique Words Count: {len(unique_words_set)}")
    print(f"   - Lexical Diversity Score: {lexical_diversity:.2f}%\n")

    # 3. Stop-words Filtering using Set Difference
    stop_words = {
        "is", "an", "and", "in", "on", "the", "like", "used", "widely",
        "vast", "models", "opens", "leverage", "specialized"
    }
    meaningful_words = [w for w in words if w not in stop_words]

    # 4. Word Frequency Distribution using Counter
    word_counts = Counter(meaningful_words)
    top_5_words = word_counts.most_common(5)

    print("🏆 Top 5 Most Frequent Meaningful Words:")
    for rank, (word, count) in enumerate(top_5_words, 1):
        print(f"   {rank}. '{word}': {count} occurrences")


# =====================================================================
# PROJECT 3: SOCIAL NETWORK MUTUAL CONNECTIONS & RECOMMENDATION ENGINE
# =====================================================================
def project_social_recommendations():
    section("3. SOCIAL NETWORK MUTUAL CONNECTIONS & RECOMMENDATION ENGINE")

    # Friend Network Graph: User -> Set of Friends
    social_graph = {
        "Alice": {"Bob", "Charlie", "David", "Eve"},
        "Bob": {"Alice", "Charlie", "Frank", "Grace"},
        "Charlie": {"Alice", "Bob", "David", "Frank"},
        "David": {"Alice", "Charlie", "Hannah"},
        "Eve": {"Alice", "Hannah"},
        "Frank": {"Bob", "Charlie"},
        "Grace": {"Bob"},
        "Hannah": {"David", "Eve"}
    }

    user_a = "Alice"
    user_b = "Bob"

    # 1. Mutual Friends using Set Intersection (&)
    alice_friends = social_graph[user_a]
    bob_friends = social_graph[user_b]
    mutual_friends = alice_friends & bob_friends

    print(f"🤝 Mutual Friends between {user_a} and {user_b}: {mutual_friends}")

    # 2. Jaccard Similarity Index = |A ∩ B| / |A ∪ B|
    union_friends = alice_friends | bob_friends
    jaccard_sim = len(mutual_friends) / len(union_friends) if union_friends else 0.0
    print(f"📐 Jaccard Similarity Coefficient ({user_a}, {user_b}): {jaccard_sim:.4f}")

    # 3. Friend Recommendation Engine for Alice
    # Find friends of Alice's friends who are NOT currently Alice's friends and NOT Alice herself
    recommendations = Counter()

    for friend in alice_friends:
        # Candidate friends of friend
        candidates = social_graph[friend] - alice_friends - {user_a}
        for candidate in candidates:
            recommendations[candidate] += 1

    print(f"\n💡 Friend Recommendations for '{user_a}' (Ranked by Mutual Connections):")
    for person, mutual_count in recommendations.most_common():
        print(f"   - Recommend '{person}' ({mutual_count} mutual connections)")


# =====================================================================
# PROJECT 4: ENTERPRISE USER ROLE-BASED ACCESS CONTROL (RBAC) SYSTEM
# =====================================================================
def project_rbac_security():
    section("4. ENTERPRISE ROLE-BASED ACCESS CONTROL (RBAC) SYSTEM")

    # Defined Immutable Role Permission Matrix using frozenset
    PERMISSIONS_VIEW = frozenset(["read:dashboard", "read:reports"])
    PERMISSIONS_EDITOR = PERMISSIONS_VIEW | frozenset(["write:content", "update:reports"])
    PERMISSIONS_ADMIN = PERMISSIONS_EDITOR | frozenset(["delete:content", "manage:users", "system:configure"])

    ROLE_MATRIX = {
        "Viewer": PERMISSIONS_VIEW,
        "Editor": PERMISSIONS_EDITOR,
        "Admin": PERMISSIONS_ADMIN
    }

    # User Assignments (A user can have multiple roles)
    user_roles = {
        "user_john": ["Viewer"],
        "user_sarah": ["Editor"],
        "user_alex": ["Editor", "Admin"]
    }

    def get_user_permissions(username: str) -> set:
        """Computes combined effective permissions for a user across all assigned roles."""
        roles = user_roles.get(username, [])
        effective_permissions = set()
        for role in roles:
            effective_permissions |= ROLE_MATRIX.get(role, frozenset())
        return effective_permissions

    def evaluate_access(username: str, required_permissions: set) -> tuple[bool, set]:
        """Evaluates whether a user satisfies required permissions, returning (Granted, Missing)."""
        user_perms = get_user_permissions(username)
        is_granted = required_permissions <= user_perms  # Subset test!
        missing_perms = required_permissions - user_perms  # Difference test!
        return is_granted, missing_perms

    # Test Access Control Requests
    target_action = {"write:content", "delete:content"}
    print(f"🔒 Security Audit: Requesting Action needing permissions: {target_action}\n")

    for user in ["user_john", "user_sarah", "user_alex"]:
        granted, missing = evaluate_access(user, target_action)
        status_str = "✅ ACCESS GRANTED" if granted else "❌ ACCESS DENIED"
        print(f"User: {user:<12} | Status: {status_str}")
        if not granted:
            print(f"   Missing Permissions: {missing}")


def main():
    project_inventory_system()
    project_text_analyzer()
    project_social_recommendations()
    project_rbac_security()


if __name__ == "__main__":
    main()
