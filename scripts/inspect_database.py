"""
Script to inspect the OKR SQLite database structure and basic statistics.
Generates a comprehensive report of tables, schemas, and data quality metrics.
"""

import sqlite3
import sys
from pathlib import Path

def inspect_database(db_path):
    """Inspect SQLite database structure and generate report."""
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("=" * 80)
    print("OPEN KHIPU REPOSITORY DATABASE INSPECTION")
    print("=" * 80)
    print()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    tables = cursor.fetchall()
    
    print(f"Total tables found: {len(tables)}")
    print()
    
    for table_name in tables:
        table = table_name[0]
        print("=" * 80)
        print(f"TABLE: {table}")
        print("=" * 80)
        
        # Get table schema
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        
        print("\nSchema:")
        print(f"{'Column':<30} {'Type':<15} {'NotNull':<10} {'Default':<15} {'PK':<5}")
        print("-" * 80)
        for col in columns:
            cid, name, ctype, notnull, default_val, pk = col
            print(f"{name:<30} {ctype:<15} {str(bool(notnull)):<10} {str(default_val):<15} {str(bool(pk)):<5}")
        
        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM {table};")
        row_count = cursor.fetchone()[0]
        print(f"\nRow count: {row_count:,}")
        
        # Get sample data (first 3 rows)
        if row_count > 0:
            cursor.execute(f"SELECT * FROM {table} LIMIT 3;")
            samples = cursor.fetchall()
            print("\nSample data (first 3 rows):")
            col_names = [desc[0] for desc in cursor.description]
            
            # Show column names
            print("\nColumns:", ", ".join(col_names))
            
            for i, row in enumerate(samples, 1):
                print(f"\nRow {i}:")
                for col_name, value in zip(col_names, row):
                    # Truncate long values
                    val_str = str(value)
                    if len(val_str) > 100:
                        val_str = val_str[:97] + "..."
                    print(f"  {col_name}: {val_str}")
        
        # Check for NULL values in each column
        print("\nNULL value counts:")
        for col in columns:
            col_name = col[1]
            cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {col_name} IS NULL;")
            null_count = cursor.fetchone()[0]
            if null_count > 0:
                null_pct = (null_count / row_count * 100) if row_count > 0 else 0
                print(f"  {col_name}: {null_count:,} ({null_pct:.1f}%)")
        
        print()
    
    conn.close()
    
    print("=" * 80)
    print("INSPECTION COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    db_path = Path(__file__).parent.parent / "khipu.db"
    
    if not db_path.exists():
        print(f"Error: Database not found at {db_path}")
        sys.exit(1)
    
    inspect_database(db_path)
