import os, sys
from os.path import dirname, abspath


SITE_ROOT = os.path.join(dirname(dirname(abspath(__file__))), "stock_management")
sys.path.insert(0, SITE_ROOT)
    
    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock_management.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
