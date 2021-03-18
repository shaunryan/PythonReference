from flask import Flask
import logging
import logging.config
import os
from . import mock

def overide_config(config, envar:list):
    for e in envar:
        if e in os.environ:        
            config[e] = os.environ.get(e)    
        
def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    # If there is a logging config override use it - otherwise use the flask default.
    # note that logging configuration is production administration so should not ship with the code
    # is using a file then in put it the the app root ./instance/logging.conf
    logging_config_file = os.path.join(app.instance_path, 'logging.cfg')
    if os.path.exists(logging_config_file):
        logging.config.fileConfig(logging_config_file)
    else:
        if test_config:
            logging_level = logging.DEBUG
        else:
            logging_level = logging.INFO
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s', level=logging_level)
        logging_config_file = None

    logger = logging.getLogger('mock')
    logger.info('Starting Flask Service')
    
    # let the world know where the logging has been configured from.
    if logging_config_file:
        logger.info(f"Logging Configuration: {logging_config_file}")
    else:
        logger.info(f"Logging Configuration: default")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile(os.path.join(app.instance_path, 'application.cfg'), silent=True)
    else:
        # load the test config if passed in
        app.config.from_pyfile(test_config, silent=True)

    # override config with environment variables
    envars = ['NONE']

    overide_config(app.config, envars)

    logger.debug(str(app.config))

    app.register_blueprint(mock.bp)

    return app

app = create_app()

            
