class UserSession:
    """Manages user authentication and permissions for the application"""

    def __init__(self):
        self.user_type = None  # "Admin", "Captain", or "User"
        self.captain_team = None  # Team name if Captain role
        self.captain_username = None  # Username if Captain role
        self.is_authenticated = False

    def set_admin(self):
        """Set the session to Admin role with full access"""
        self.user_type = "Admin"
        self.is_authenticated = True
        self.captain_team = None
        self.captain_username = None

    def set_captain(self, username, team_name):
        """Set the session to Captain role with team-specific access"""
        self.user_type = "Captain"
        self.captain_username = username
        self.captain_team = team_name
        self.is_authenticated = True

    def set_user(self):
        """Set the session to User role with read-only access"""
        self.user_type = "User"
        self.is_authenticated = True
        self.captain_team = None
        self.captain_username = None

    def logout(self):
        """Clear the session and log out the current user"""
        self.user_type = None
        self.captain_team = None
        self.captain_username = None
        self.is_authenticated = False

    def is_admin(self):
        """Check if the current user is an Admin"""
        return self.user_type == "Admin"

    def is_captain(self):
        """Check if the current user is a Captain"""
        return self.user_type == "Captain"

    def is_user(self):
        """Check if the current user is a regular User"""
        return self.user_type == "User"

    def can_edit_player(self, player_team_name):
        """
        Check if the current user can edit a player on the specified team

        Args:
            player_team_name: The team name the player belongs to

        Returns:
            True if user can edit, False otherwise
        """
        if self.is_admin():
            return True
        if self.is_captain() and player_team_name == self.captain_team:
            return True
        return False

    def should_hide_sensitive_fields(self, player_team_name):
        """
        Check if sensitive fields (dob, address, phone, email) should be hidden

        Args:
            player_team_name: The team name the player belongs to

        Returns:
            True if fields should be hidden, False otherwise
        """
        if self.is_admin():
            return False
        if self.is_captain() and player_team_name == self.captain_team:
            return False
        # User or Captain viewing other team
        return True


# Module-level singleton instance
_session = UserSession()


def get_session():
    """Get the singleton session instance"""
    return _session
