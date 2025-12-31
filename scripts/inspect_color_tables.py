"""
Script to inspect color-related tables in the OKR database.
"""

import sqlite3
from pathlib import Path

def inspect_color_tables(db_path):
    """Inspect color-related tables in detail."""
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    color_tables = [
        'ascher_cord_color',
        'ascher_canutito_color', 
        'ascher_canuto_color',
        'ascher_color_dc',
        'color_operator_dc'
    ]
    
    for table_name in color_tables:
        print("=" * 80)
        print(f"TABLE: {table_name}")
        print("=" * 80)
        
        # Get schema
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        print("\nSchema:")
        for col in columns:
            cid, name, ctype, notnull, default_val, pk = col
            print(f"  {name} ({ctype})")
        
        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        row_count = cursor.fetchone()[0]
        print(f"\nRow count: {row_count:,}")
        
        # Get sample data
        if row_count > 0:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 10;")
            samples = cursor.fetchall()
            col_names = [desc[0] for desc in cursor.description]
            
            print(f"\nSample data (first {min(10, row_count)} rows):")
            for i, row in enumerate(samples, 1):
                print(f"\nRow {i}:")
                for col_name, value in zip(col_names, row):
                    print(f"  {col_name}: {value}")
        
        print()
    
    conn.close()

if __name__ == "__main__":
    db_path = Path(__file__).parent.parent / "khipu.db"
    inspect_color_tables(db_path)
