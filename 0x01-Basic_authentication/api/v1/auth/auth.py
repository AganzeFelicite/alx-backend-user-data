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
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != "/":
            path = path + "/"
        for patterns in excluded_paths:
            if path[-1] == "*":
                if patterns.startswith(path[:-1]):
                    return False
            if path == patterns:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        dealing with the authorization header
        """
        if request is None:
            return None
        authorization = request.headers.get("Authorization")
        if authorization is None:
            return None
        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """
        this returns the current loggin
        user
        """
        return None
