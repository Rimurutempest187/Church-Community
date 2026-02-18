# check_db.py
import sqlite3
conn = sqlite3.connect("data/bot.db")
cur = conn.cursor()
print("quizzes:", cur.execute("SELECT COUNT(*) FROM quizzes").fetchone()[0])
print("verses:", cur.execute("SELECT COUNT(*) FROM verses").fetchone()[0])
print("sample quiz:", cur.execute("SELECT id, question FROM quizzes LIMIT 1").fetchone())
conn.close()
