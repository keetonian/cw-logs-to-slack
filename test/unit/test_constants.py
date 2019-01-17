"""Constants used for unit tests.

This can be used to define values for environment variables so unit tests can use these to assert on expected values.
"""

SLACK_URL = 'url'

AWS_LOG_EVENT = {
    "awslogs":
    {
        "data": "H4sIAAAAAAAAAHWPwQqCQBCGX0Xm7EFtK+smZBEUgXoLCdMhFtKV3akI8d0bLYmibvPPN3wz00CJxmQnTO41whwWQRIctmEcB6sQbFC3CjW3XW8kxpOpP+OC22d1Wml1qZkQGtoMsScxaczKN3plG8zlaHIta5KqWsozoTYw3/djzwhpLwivWFGHGpAFe7DL68JlBUk+l7KSN7tCOEJ4M3/qOI49vMHj+zCKdlFqLaU2ZHV2a4Ct/an0/ivdX8oYc1UVX860fQDQiMdxRQEAAA=="
    }
 }

EXTRACTED_LOG_EVENTS = [{'id': 'eventId1', 'timestamp': 1440442987000, 'message': '[ERROR] First test message'}, {'id': 'eventId2', 'timestamp': 1440442987001, 'message': '[ERROR] Second test message'}]
