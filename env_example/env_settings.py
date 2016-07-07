SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_TWITCH_KEY = 'YOUR TWITCH KEY'
SOCIAL_AUTH_TWITCH_SECRET = 'YOUR TWITCH SECRET'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard/'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_USER_MODEL = 'auth.User'
SOCIAL_AUTH_TWITCH_SCOPE = [
    'user_read',
    'user_blocks_edit',
    'user_blocks_read',
    'user_follows_edit',
    'channel_read',
    'channel_editor',
    'channel_commercial',
    'channel_stream',
    'channel_subscriptions',
    'user_subscriptions',
    'channel_check_subscription',
    'chat_login'
]