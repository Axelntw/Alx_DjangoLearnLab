LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
INSTALLED_APPS = [
    'relationship_app',
]

AUTH_USER_MODEL = 'relationship_app.CustomUser'