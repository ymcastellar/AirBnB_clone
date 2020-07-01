#!/usr/bin/python3
"""Review of the place. Public class attributes: place_id,
    user_id and text
"""
from models.base_model import BaseModel


class Review(Basemodel):
    """ inheritated class Review from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
