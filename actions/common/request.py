"""Common file for handling requests.
"""
import requests
from common.constants import ADDRESS


def get_location(part):
    """ Get the current location of a part.
    """
    request = requests.get('http://%s/v1/arm/%s' % (ADDRESS, part))

    return request.json()


def set_location(part, location):
    """ Get the current location of a part.
    """
    request = requests.put(
        'http://%s/v1/arm/%s' % (ADDRESS, part),
        json={'location': location}
    )

    return request.json()


def set_torque(part, state):
    """ Get the current location of a part.
    """
    request = requests.put(
        'http://%s/v1/arm/%s/torque' % (ADDRESS, part),
        json={'state': state}
    )

    return request.json()
