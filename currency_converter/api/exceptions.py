"""Exceptions storage."""


class NotOKStatusCodeException(Exception):
    """Raise when api status-code != 200."""


class NoResponse(Exception):
    """Raise when cannot get the api-answer."""


class NoCurrency(Exception):
    """Raise when there's no that currency."""


class NoJSON(Exception):
    """Raise when there's not a json-format."""
