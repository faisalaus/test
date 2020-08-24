# python -m venv name
# To create the envoirnment
# Control Space short cut for Json Settings
# git and vs code
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greeting(who_to_greet):
    return f"hello{who_to_greet}"


r = requests.get("https://www.youtube.com/watch?v=-nh9rCzPJ20")
print(r.status_code)
