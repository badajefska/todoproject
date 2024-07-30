import sqlite3

# SQLiteデータベースの作成（もしくは既存のデータベースファイルを指定）
db_file = "mywork.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# テーブルの作成
cursor.execute("""
    CREATE TABLE IF NOT EXISTS work_records (
        id INTEGER PRIMARY KEY,
        Date DATE,
        OverTime TEXT,
        Vehicle TEXT,
        WorkName TEXT
    )
""")

# データの挿入
def insert_record(Date, OverTime, Vehicle, WorkName):
    cursor.execute("""
        INSERT INTO work_records (Date, OverTime, Vehicle, WorkName)
        VALUES (?, ?, ?, ?)
    """, (Date, OverTime, Vehicle, WorkName))
    conn.commit()

# ユーザーとの対話
while True:
    Date = input("日付を入力してください (YYYY-MM-DD): ")
    OverTime = input("残業時間を入力してください (HH:MM): ")
    Vehicle = input("車輛番号を入力してください: ")
    WorkName = input("作業名を入力してください: ")

    insert_record(Date, OverTime, Vehicle, WorkName)
    print("作業記録が追加されました！")

    choice = input("作業記録を続けますか？ (y/n): ")
    if choice.lower() != "y":
        break

# データベース接続を閉じる
conn.close()


