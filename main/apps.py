from django.apps import AppConfig
# TODO: Разобраться с этим потом
#from django.dispatch import Signal
#from utilities import send_activation_email
#
# user_registered = Signal()
#
#
# def user_registered_dispatcher(sender, **kwargs):
#     send_activation_email(kwargs['instance'])
#
#
# user_registered.connect(user_registered_dispatcher)


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
