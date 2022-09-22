import sqlite3
from sqlite3 import Error
from pprint import pprint


def create_connection(path: str):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'sqlite connection error {e}')

    return connection


def execute_query(connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'sqlite connection error {e}')


connection = create_connection('my_db.sqlite')

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    location TEXT
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# execute_query(connection, create_users_table)
# execute_query(connection, create_posts_table)

create_comments_table = """
    CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (user_id) REFERENCES posts (id)
);
"""

create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (user_id) REFERENCES posts (id)
);
"""
# execute_query(connection, create_comments_table)
# execute_query(connection, create_likes_table)

create_users = """
INSERT INTO
    users (name, age, gender, location)
 VALUES 
    ('Oleg', 31, 'male', 'Zhmerynka'),
    ('Lev', 18, 'male', 'Chernivtsi'),
    ('Tetiana', 24, 'female', 'Poltava');
"""

create_posts = """
INSERT INTO
    posts (title, description, user_id)
VALUES 
    ('YOUR WELLCOME', 'GOOD TO SEE YA FRIEND', 2),   
    ('FIRST DAY AUTUMN', 'HAVE A NICE DAY GUYS', 3),   
    ('I NEED HELP IN TREE GRAPH ON PYTHON', 'SOME ERROR IN CODE', 1);   
"""
# execute_query(connection, create_users)
# execute_query(connection, create_posts)

create_comments = """
INSERT INTO
    comments (text, user_id, post_id)
VALUES 
    ('i will try help u', 2, 3),
    ('me to ha-ha-ha', 1, 1),
    ('Iam ready', 3, 2);
"""

create_likes = """
INSERT INTO
    likes (user_id, post_id)
VALUES 
    (2, 2),
    (1, 3),
    (3, 1);
"""

# execute_query(connection, create_comments)
# execute_query(connection, create_likes)


def select_query(connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'sqlite connection error {e}')


select_users = "SELECT name, id, age from users"

users = select_query(connection, select_users)

# pprint(users)

posts = select_posts = "SELECT * from posts"
posts = select_query(connection, posts)

# pprint(posts)

select_users_posts = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
INNER JOIN users on users.id = posts.user_id
"""

users_posts = select_query(connection, select_users_posts)

# pprint(users_posts)

select_posts_comments_users = """
SELECT
    posts.description as post,
    text as comment,
    name
FROM
    posts
    INNER JOIN comments on posts.id = comments.user_id
    INNER JOIN users on users.id = comments.user_id
"""
# result = select_query(connection, select_posts_comments_users)
# pprint(result)

where_select = "SELECT description FROM posts WHERE id = 2"
result = select_query(connection, where_select)
pprint(result)