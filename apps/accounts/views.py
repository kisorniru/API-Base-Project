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
    return success_response(token_payload(1, 'example-token'), message='Logged in')
