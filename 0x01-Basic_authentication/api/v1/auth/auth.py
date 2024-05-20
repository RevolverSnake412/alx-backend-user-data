#!/usr/bin/env python3
"""
auth
"""
from typing import List, TypeVar
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header
        """
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user
        """
        return None
