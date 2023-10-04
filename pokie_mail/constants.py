# Version
POKIE_MAIL_VERSION = ["1", "0", "0"]


def get_version():
    return ".".join(POKIE_MAIL_VERSION)

# Service names

SVC_MESSAGE_QUEUE = "sv_pokie_mail_msg_queue"
SVC_MESSAGE_TEMPLATE = "sv_pokie_mail_msg_template"
