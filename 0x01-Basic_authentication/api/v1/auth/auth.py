#!/usr/bin/env python3
"""
a class that will manage api
authentication
"""


from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """
    this is an auth class
    """
    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]
                     ) -> bool:
        """
        requires auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        dealing with the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        this returns the current loggin
        user
        """
        return None
