from apps.accounts.services import AuthService
from apps.core.responses import success_response

def token_payload(user_id, access_token, refresh_token=None):
    payload = {
        'user_id': user_id,
        'token_type': 'Bearer',
        'access_token': access_token,
    }
    if refresh_token:
        payload['refresh_token'] = refresh_token
    return payload

def login(request):
    token = AuthService().issue_example_token()
    return success_response(token_payload(token.user_id, token.access_token), message='Logged in')

def current_user(request):
    return success_response({'id': 1, 'name': 'Example User'}, message='Current user')

def logout(request):
    return success_response(message='Logged out')
