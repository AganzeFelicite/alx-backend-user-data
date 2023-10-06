#!/usr/bin/env python3
"""
BasicAuth class
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    doing nothing for
    now
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """
        this this is to convert to 64bytes
        encoded data format
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
