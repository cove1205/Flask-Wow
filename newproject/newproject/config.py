class BaseConfig(object):
    """Base config"""

    SECRET_KEY = 'basic'
    DEBUG = False

class ProductionConfig(BaseConfig):
    """Use production Config."""




class DevelopmentConfig(BaseConfig):
    """Use development Config."""

    DEBUG = True


config = {
 'development': DevelopmentConfig,
 'production': ProductionConfig,
 'default': DevelopmentConfig
}