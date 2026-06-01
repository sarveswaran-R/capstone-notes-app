import sys
import psycopg2

conn = psycopg2.connect(dbname="capstone", user="postgres", host="/var/run/postgresql", password="postgres")
with conn.cursor() as cur:
      if len(sys.argv) > 1:
          cur.execute("INSERT INTO notes (body) VALUES (%s);", (sys.argv[1],))
          conn.commit()
      cur.execute("SELECT id, body, created_at FROM notes ORDER BY id DESC;")
      for row in cur.fetchall():
          print(row)
conn.close()
