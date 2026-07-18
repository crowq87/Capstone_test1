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
cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public' AND tablename='core_passwordresetcode';")
print('table_exists:', cur.fetchone() is not None)
cur.execute("SELECT app, name FROM django_migrations WHERE app='core' ORDER BY name")
print('migrations:', cur.fetchall())
cur.close()
conn.close()
