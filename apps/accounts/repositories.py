class UserRepository:
    """Example repository boundary for user data access."""

    def find_display_user(self, user_id):
        return {'id': user_id, 'name': 'Example User'}
