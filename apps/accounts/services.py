from dataclasses import dataclass

@dataclass
class AuthToken:
    user_id: int
    access_token: str

class AuthService:
    def issue_example_token(self, user_id=1):
        return AuthToken(user_id=user_id, access_token='example-token')
