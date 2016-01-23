# 1. Set utf-8 encoding.
# -*- coding: utf-8 -*-

# 2. Imports from rosette.api.
from rosette.api import API, DocumentParameters


def main(name, alt_url='https://api.rosette.com/rest/v1/'):
    # 3. Create API object.
    api = API("4a2ce33afde2071fd73b8c8f3977e4ea", alt_url)
    params = DocumentParameters()
    params["content"] = name
    return api.entities(params, True)  # entity linking is turned on
