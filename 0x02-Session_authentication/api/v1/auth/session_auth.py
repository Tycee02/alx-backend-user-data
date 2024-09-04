#!/usr/bin/env python3
"""Session authentication for API
"""
from uuid import uuid4
from flask import request

from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session Authentication class
    """
