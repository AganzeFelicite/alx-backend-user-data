#!/usr/bin/env python3
"""
this is about session management in
python/ apis
"""


from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    session auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        instance method to create a sessesion
        for a user with the specified user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        this return the user id based on the session_id
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
