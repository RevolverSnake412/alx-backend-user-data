#!/usr/bin/env python3
"""
encryp_password
"""
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    returns a hashed password
    """
    encoded_password = password.encode()
    hashed_password = hashpw(encoded_password, bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    return a bool, checks if valid or not.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
