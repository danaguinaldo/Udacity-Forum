# "Database code" for the DB Forum.
import psycopg2
import datetime

def get_posts():
  db = psycopg2.connect(database="forum")
  c = db.cursor()
  c.execute("SELECT content, time FROM posts ORDER BY time desc;")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database="forum")
  c = db.cursor()
  c.execute("INSERT INTO posts VALUES ('%s');" % content) # Almost but not quite.
  db.commit()
  db.close()
