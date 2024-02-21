from opentelemetry import metrics

# In this file, asynchronous instruments are defined and created
# For a detailed description, see the OpenTelemetry docs:
#    https://opentelemetry.io/docs/languages/python/instrumentation/#creating-and-using-asynchronous-instruments

homepage_meter = metrics.get_meter("homepage")


def create_async_instruments():
    """
    Register asynchronous instruments with OpenTelemetry
    """
    pass
