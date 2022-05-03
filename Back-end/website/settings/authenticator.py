AUTH_USER_MODEL = 'authenticator.User'  # For authenticator
REST_FRAMEWORK = {  # For authenticator
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {  # For authenticator
   'AUTH_HEADER_TYPES': ('JWT',),
}

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'authenticator.serializers.UserCreateSerializer',
        'user': 'authenticator.serializers.UserRetrieveSerializer',
    }
}
