from mrsage.django.deployment_configuration.core import generate_deployment_settings


def test_generate_deployment_settings(deployment_settings_module):
    generate_deployment_settings(deployment_settings_module)
