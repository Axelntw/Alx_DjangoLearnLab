INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SECRET_KEY = 'your-secret-key-here'  # Replace with a real secret key

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Security settings
DEBUG = False  # Disable debug mode in production

# XSS protection
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS protection

# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'  # Prevent site from being embedded in iframes

# MIME type sniffing security protection
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing

# CSRF and session security
CSRF_COOKIE_SECURE = True  # Send CSRF cookie only via HTTPS
SESSION_COOKIE_SECURE = True  # Send session cookie only via HTTPS

# HTTPS enforcement
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains
SECURE_HSTS_PRELOAD = True  # Allow preloading of HSTS by browsers

# Content Security Policy
CSP_DEFAULT_SRC = ("'self'",)  # Default to same-origin policy for all content
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  # Allow inline styles
CSP_SCRIPT_SRC = ("'self'",)  # Allow scripts only from same origin
CSP_IMG_SRC = ("'self'",)  # Allow images only from same origin
CSP_FONT_SRC = ("'self'",)  # Allow fonts only from same origin

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')