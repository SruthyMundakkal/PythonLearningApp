import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnpy.settings')

# Create the WSGI application that Vercel will use
application = get_wsgi_application()

# Vercel expects either 'app' or 'handler', so we export 'app'
app = application
