"""
============================
Project application composer
============================

Composer is able to define settings, urls and package requirements from a selection of
applications.

"""
import importlib
import json
import sys


class EnabledComposableApplication:
    """
    Empty class to mark a settings class mixin as enabled to load for composition.

    This class won't never ever introduce anything else than marker attribute
    ``_ENABLED_COMPOSABLE_APPLICATION`` since the class may be herited by any kind of
    class we don't want to pollute.

    Only purpose of attribute ``_ENABLED_COMPOSABLE_APPLICATION`` is to mark it for
    inspection from composer.
    """
    _ENABLED_COMPOSABLE_APPLICATION = True


def import_module(name, package=None):
    """
    An approximate implementation of import taken from Python importlib documentation.

    This will import a module from given python path in name argument. package argument
    can be given to search in. If module is not in current directory, you will have to
    add its parent path in sys.path. Also relative module path will work only for
    inside a package.
    """
    absolute_name = importlib.util.resolve_name(name, package)
    try:
        return sys.modules[absolute_name]
    except KeyError:
        pass

    path = None
    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)
        path = parent_module.__spec__.submodule_search_locations
    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)
        if spec is not None:
            break
    else:
        msg = f'No module named {absolute_name!r}'
        raise ModuleNotFoundError(msg, name=absolute_name)

    module = importlib.util.module_from_spec(spec)
    sys.modules[absolute_name] = module
    spec.loader.exec_module(module)

    if path is not None:
        setattr(parent_module, child_name, module)

    return module


class ComposerAbstract:
    """
    Composer abstract implements everything about application module discovery.
    """
    def __init__(self, manifest_path, apps_pythonpath, base_paths=None):
        self.manifest_path = manifest_path
        self.apps_pythonpath = apps_pythonpath
        self.manifest = self.get_manifest(self.manifest_path)
        self.apps = self.manifest["apps"]

        for item in (base_paths or []):
            sys.path.append(item)


    def get_manifest(self, path):
        """
        Load manifest from JSON file and return it as Python object (dict expected).
        """
        return json.loads(path.read_text())

    def find_app_module(self, name):
        try:
            module = import_module(name)
        except ModuleNotFoundError:
            print("Unable to find module: {}".format(name))
            return None
        else:
            return module


class ApplicationUrlCollector:
    """
    Application urls collector
    """
    def __init__(self, settings=None):
        self.settings = settings

    def load_urlpatterns(self, urlpatterns):
        """
        Method to implement by Application Url classes.

        Every classes should not forget to use ``super().load_urlpatterns(urlpatterns)``
        in their ``load_urlpatterns`` method implementation, commonly at the beggining.
        """
        return urlpatterns

    def mount(self, urlpatterns):
        print("🎨 ApplicationUrlMounter Collecting urls")
        patterns = self.load_urlpatterns(urlpatterns)

        # Debug
        print()
        for item in patterns:
            print("*", item)
        print()

        return patterns
