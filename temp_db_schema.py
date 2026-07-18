import os
import django
from dotenv import load_dotenv
load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autohub.settings')
django.setup()
import psycopg2
from django.conf import settings
conn = psycopg2.connect(
    dbname=settings.DATABASES['default']['NAME'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    host=settings.DATABASES['default']['HOST'],
    port=settings.DATABASES['default']['PORT'],
    sslmode=settings.DATABASES['default']['OPTIONS'].get('sslmode', 'require')
)
cur = conn.cursor()
for table in ['core_userprofile','core_vehiclelisting','core_passwordresetcode']:
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name=%s ORDER BY ordinal_position", (table,))
    cols = [row[0] for row in cur.fetchall()]
    print(table, cols)
cur.close()
conn.close()
