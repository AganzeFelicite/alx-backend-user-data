#!/usr/bin/env python3
"""
BasicAuth class
"""

from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        a method that is going to decode from the base64
        byte encode type
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encode = base64_authorization_header.encode('utf-8')
            base = base64.b64decode(encode)
            return base.decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        extract the user info basic on the
        authorizationheader sent
        encoded in base64
        """
        b64auth = decoded_base64_authorization_header
        if b64auth is None:
            return (None, None)
        if (not isinstance(b64auth, str) or ":" not in b64auth):
            return (None, None)

        userValues = b64auth.split(":", 1)
        return (userValues[0], userValues[1])
