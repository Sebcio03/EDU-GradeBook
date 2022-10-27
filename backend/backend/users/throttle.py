from rest_framework.throttling import AnonRateThrottle


class SignUpThrottle(AnonRateThrottle):
    rate = "30/min"
