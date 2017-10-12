from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class DenememoduleConfig(ModuleMixin, AppConfig):
    name = 'denememodule'
    icon = '<i class="material-icons">settings_applications</i>'
