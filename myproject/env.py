import os

os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DEBUG'] = 'True'

os.environ['DB_NAME'] = 'mydb'
os.environ['DB_USER'] = 'postgres'
os.environ['DB_PASSWORD'] = 'admin'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '5432'