
import sqlite3
import pandas as pd

DB_FILE = "oldest_living_players_cleaned.csv"

def show_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [t[0] for t in cursor.fetchall()]
    print("\n📄 Available tables in the database:")
    for t in tables:
        print(f"  • {t}")
    print()

def query_loop():
    print("📊 Welcome to the MLB History Database Query Tool")
    print("Type SQL queries to explore the data, or type 'exit' to quit.\n")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    show_tables(cursor)

    while True:
        try:
            user_input = input("SQL> ").strip()
            if user_input.lower() in ("exit", "quit"):
                print("👋 Goodbye!")
                break
            if not user_input.endswith(";"):
                user_input += ";"

            # Run query
            df = pd.read_sql_query(user_input, conn)
            if df.empty:
                print("🔍 Query returned no results.\n")
            else:
                print("\n✅ Results:")
                print(df.head(20).to_string(index=False))  # Show top 20 rows
                print(f"\n📦 {len(df)} rows returned.\n")

        except Exception as e:
            print(f"Error: {e}\n")

    conn.close()

if __name__ == "__main__":
    query_loop()


# 1. View the First Few Players
# SELECT * FROM oldest_living_players_cleaned LIMIT 10;

#  2. Find the Oldest Living Player
# SELECT Name, Age, "Birth Date", "Team" FROM oldest_living_players_cleaned ORDER BY CAST(SUBSTR(Age, 1, INSTR(Age, ' ') - 1) AS INTEGER) DESC LIMIT 2

# 3. Players Who Debuted Before 1950     
# SELECT Name, Debut, "Final Game", Team FROM oldest_living_players_cleaned WHERE Debut < '1950'
    
# 4. Count of Players by Debut Decade
# SELECT SUBSTR(Debut, 1, 3) || '0s' AS Decade, COUNT(*) AS PlayerCount FROM oldest_living_players_cleaned WHERE Debut IS NOT NULL AND Debut != '' GROUP BY Decade ORDER BY Decade
    
# 5. Players Who Played for a Specific Team
# SELECT Name, Team, Debut, "Final Game" FROM oldest_living_players_cleaned WHERE Team LIKE '%Yankees%' 
    
# 6. Get All Profile Links
# SELECT Name, "Profile Link" FROM oldest_living_players_cleaned WHERE "Profile Link" IS NOT NULL AND "Profile Link" != ''
    
# 7. Players With Long Careers (10+ years)
# SELECT Name, Debut, "Final Game", (CAST(SUBSTR("Final Game", 1, 4) AS INTEGER) - CAST(SUBSTR(Debut, 1, 4) AS INTEGER)) AS CareerLength FROM oldest_living_players_cleaned WHERE Debut IS NOT NULL AND "Final Game" IS NOT NULL AND CareerLength >= 10 ORDER BY CareerLength DESC
      
