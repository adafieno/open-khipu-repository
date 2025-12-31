import sqlite3

conn = sqlite3.connect('khipu.db')
cursor = conn.cursor()

print("Sample knot encodings:")
print("-" * 80)

cursor.execute("""
    SELECT CORD_ID, TYPE_CODE, knot_value_type, NUM_TURNS, DIRECTION 
    FROM knot 
    WHERE knot_value_type IS NOT NULL 
    LIMIT 20
""")

print(f"{'CORD_ID':>8} | {'TYPE':>4} | {'VALUE':>5} | {'TURNS':>5} | {'DIR':>4}")
print("-" * 80)

for row in cursor.fetchall():
    cord_id, type_code, value, turns, direction = row
    turns_str = f"{turns:.0f}" if turns is not None else "NULL"
    print(f"{cord_id:>8} | {type_code:>4} | {value:>5} | {turns_str:>5} | {direction:>4}")

print()
print("=" * 80)
print("Checking distribution of knot_value_type:")

cursor.execute("""
    SELECT knot_value_type, COUNT(*) as count
    FROM knot
    WHERE knot_value_type IS NOT NULL
    GROUP BY knot_value_type
    ORDER BY count DESC
    LIMIT 15
""")

print(f"{'VALUE':>6} | {'COUNT':>8}")
print("-" * 80)
for value, count in cursor.fetchall():
    print(f"{value:>6} | {count:>8,}")

conn.close()
