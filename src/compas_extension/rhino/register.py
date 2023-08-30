import os
from compas.plugins import plugin

from compas_ui.values import Settings
from compas_ui.values import BoolValue
from compas_ui.values import FloatValue

HERE = os.path.dirname(__file__)

SETTINGS = Settings(
    {
        "some_global_settings.a": BoolValue(True),
        "some_global_settings.b": FloatValue(0.1),
    }
)


@plugin(category="ui")
def register(ui):
    ui.registry["PLUGIN_NAME_create_beam"] = SETTINGS
