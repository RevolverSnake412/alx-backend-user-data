#!/usr/bin/env python3
"""
basic_auth.py
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    pass
