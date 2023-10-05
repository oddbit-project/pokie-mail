from rick.resource.config import EnvironmentConfig
from pokie.config.template import BaseConfigTemplate, PgConfigTemplate, TestConfigTemplate
from pokie.core import FlaskApplication
from pokie.core.factories.pgsql import PgSqlFactory

from pokie_mail.config import MailConfigTemplate


# base configuration
class Config(EnvironmentConfig, BaseConfigTemplate, PgConfigTemplate, TestConfigTemplate, MailConfigTemplate):
    TEST_MANAGE_DB = True
    TEST_DB_SSL = False

    # number of emails to send at once
    MAILS_PER_RUN = 10000

    # SMTP Configuration [to use with mailhog]
    SMTP_HOST = "localhost"
    SMTP_PORT = 1025
    SMTP_USE_TLS = False
    SMTP_USE_SSL = False
    SMTP_DEBUG = False
    SMTP_USERNAME = ""
    SMTP_PASSWORD = ""
    SMTP_DEFAULT_SENDER = None
    SMTP_TIMEOUT = None
    SMTP_SSL_KEYFILE = None
    SMTP_SSL_CERTFILE = None


def build_pokie():
    # load configuration from ENV
    cfg = Config().build()

    # modules to load & initialize
    modules = [
        'pokie_mail'
    ]

    # factories to run
    factories = [PgSqlFactory]

    # build app
    pokie_app = FlaskApplication(cfg)
    flask_app = pokie_app.build(modules, factories)
    return pokie_app, flask_app


main, app = build_pokie()

# =============================================================================

if __name__ == '__main__':
    main.cli()
