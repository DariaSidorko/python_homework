
import sqlite3

# Task 1: Create a New SQLite Database

# Connect to a new SQLite database
# with  sqlite3.connect("../db/magazines.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
#     print("Database created and connected successfully.")


# Task 2: Define Database Structure

def create_tables():
    try:
        with sqlite3.connect("../db/magazines.db") as conn:
            conn.execute("PRAGMA foreign_keys = 1")
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
            )
            """)

            print("Tables created successfully.")

    except sqlite3.Error as e:
        print("An error occurred:", e)

# create_tables()


# Task 3: Add data functions

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.Error as e:
        print("Publisher error:", e)

def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        pub_id = cursor.fetchone()
        if pub_id:
            cursor.execute("INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, pub_id[0]))
    except sqlite3.Error as e:
        print("Magazine error:", e)

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("""
            SELECT * FROM subscribers WHERE name = ? AND address = ?
        """, (name, address))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.Error as e:
        print("Subscriber error:", e)

def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
    try:
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
        sub_id = cursor.fetchone()

        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        mag_id = cursor.fetchone()

        if sub_id and mag_id:
            cursor.execute("""
                INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
            """, (sub_id[0], mag_id[0], expiration_date))
    except sqlite3.Error as e:
        print("Subscription error:", e)

def populate_data():
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Add publishers
        add_publisher(cursor, "Time Inc.")
        add_publisher(cursor, "Conde Nast")
        add_publisher(cursor, "National Geographic Society")

        # Add magazines
        add_magazine(cursor, "Time", "Time Inc.")
        add_magazine(cursor, "Vogue", "Conde Nast")
        add_magazine(cursor, "National Geographic", "National Geographic Society")

        # Add subscribers
        add_subscriber(cursor, "Alice", "123 Maple Street")
        add_subscriber(cursor, "Bob", "456 Oak Avenue")
        add_subscriber(cursor, "Charlie", "789 Pine Road")

        # Add subscriptions
        add_subscription(cursor, "Alice", "Time", "2025-12-31")
        add_subscription(cursor, "Bob", "Vogue", "2025-06-30")
        add_subscription(cursor, "Charlie", "National Geographic", "2026-01-15")

        conn.commit()
        print("Sample data inserted.")

# populate_data()


#  Task 4: SQL queries

def run_queries():
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()

        print("\nAll subscribers:")
        for row in cursor.execute("SELECT * FROM subscribers"):
            print(row)

        print("\nAll magazines sorted by name:")
        for row in cursor.execute("SELECT * FROM magazines ORDER BY name"):
            print(row)

        print("\nMagazines by 'Conde Nast':")
        cursor.execute("""
            SELECT magazines.name 
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.publisher_id
            WHERE publishers.name = 'Conde Nast'
        """)
        for row in cursor.fetchall():
            print(row)

# run_queries()
            
