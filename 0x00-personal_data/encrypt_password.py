#!/usr/bin/env python3
"""
this is a function that
will be hashing  the password
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    hashes a password using bcrypt
    """
    password = password.encode()
    hash_passwd = bcrypt.hashpw(password, bcrypt.gensalt(12))
    return hash_passwd
