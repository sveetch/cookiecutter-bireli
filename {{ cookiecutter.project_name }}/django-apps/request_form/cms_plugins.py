"""
CMS Plugins installations
"""
from cms.plugin_pool import plugin_pool

from .plugins.request import RequestPlugin

plugin_pool.register_plugin(RequestPlugin)
