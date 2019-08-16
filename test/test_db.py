import os

import psycopg2

db_url = os.environ.get('DATABASE_URL')

try:
    conn = psycopg2.connect(db_url)
except:
    print('NOT OK')
    print(db_url)
    exit(1)

print('DB OK')
exit(0)
