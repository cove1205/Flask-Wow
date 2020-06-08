import os
from flask import Flask

def create_app(conf_name=None):

    app = Flask(__name__, instance_relative_config=True)

    # TODO
    def update_config(app):
        """Update app's config"""

        from .config import config
        if conf_name is not None:
            app.config.from_object(config[conf_name])
        else:
            app.config.from_object(config["default"])

        pass

    # TODO
    def configure_logging(app):
        """Update logger's configurations"""

        pass


    def register_blueprints(app):
        """Configures blueprint.

        e.g.
        from .apps.demo import bp
        bp.register(self)
        """

        from .apps.demo import bp
        app.register_blueprint(bp)

        pass


    def configure_extensions(app):
        """Configures the extensions.

        e.g.
        mail.init_app(app)

        """

        pass

    def configure_handlers(app):
        """Configures the handlers or middleware

        """

        # from .handlers import error_handler
        # app.register_error_handler(Exception, error_handler)

        pass

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        # os.makedirs(os.path.join(self.instance_path, "logs"))
    except OSError:
        pass

    # Initialization flask app
    update_config(app)
    configure_logging(app)
    configure_handlers(app)
    configure_extensions(app)
    register_blueprints(app)

    return app






