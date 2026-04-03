import json
import subprocess
import sys

from importlib.metadata import distributions

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(staff_member_required, name="dispatch")
class StackInfoView(TemplateView):
    """
    Display Python and Node.js stack information.
    """
    template_name = "project_utils/stack_info.html"

    def get_backend_infos(self):
        """
        Get list of installed Python packages with versions.

        Returns a list of all package versions.
        """
        return sorted(
            [
                {"name": pkg.metadata["Name"], "version": pkg.metadata["Version"]}
                for pkg in distributions()
            ],
            key=lambda x: x["name"].lower()
        )

    def get_nodejs_version(self):
        """
        Call 'Node.js' executable to ask for its version.

        Returns:
            string: The Node.js version if executable can be reached.
        """
        try:
            result = subprocess.run(
                ["node", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        else:
            if result.returncode == 0:
                return result.stdout.strip()

        return None

    def get_npm_version(self):
        """
        Call 'NPM' interpreter to ask for its version.

        Returns:
            string: The NPM version if executable can be reached.
        """
        try:
            result = subprocess.run(
                ["npm", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        else:
            if result.returncode == 0:
                return result.stdout.strip()

        return None

    def get_frontend_infos(self):
        """
        Get Node.js and npm versions.

        First tries to read from node_stack.json (generated during CI build),
        then falls back to running node/npm commands if available.
        """
        node_info = {
            "node_version": self.get_nodejs_version(),
            "npm_version": self.get_npm_version(),
            "packages": [],
            "from_cache": False,
        }

        # First, try to read from cached file (generated during CI build)
        if settings.FRONTEND_BUILT_MANIFEST.exists():
            try:
                with settings.FRONTEND_BUILT_MANIFEST.open("r") as f:
                    cached_info = json.load(f)
                    node_info.update(cached_info)
                    node_info["from_cache"] = True
                    return node_info
            except Exception:
                pass

        # If there is not cached file, try to directly get packages from 'package.json'
        try:
            if settings.FRONTEND_PACKAGES_MANIFEST.exists():
                with settings.FRONTEND_PACKAGES_MANIFEST.open("r") as f:
                    package_data = json.load(f)

                    # Append production packages first
                    deps = package_data.get("dependencies", {})
                    for name, version in deps.items():
                        node_info["packages"].append({
                            "name": name,
                            "version": version,
                            "dev": False
                        })

                    # Append development packages
                    dev_deps = package_data.get("devDependencies", {})
                    for name, version in dev_deps.items():
                        node_info["packages"].append({
                            "name": name,
                            "version": version,
                            "dev": True
                        })

                    # Order packages on their development mode ('prod' first then 'dev')
                    # then on their name
                    node_info["packages"].sort(
                        key=lambda x: (x["dev"], x["name"].lower()),
                    )
        except Exception:
            pass

        return node_info

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the Python version without additional infos (build, plateform, etc..)
        context["python_version"] = "{}.{}.{}".format(*sys.version_info[:3])

        # Discover package versions
        context["python_packages"] = self.get_backend_infos()

        # Get the frontend versions
        context["node_info"] = self.get_frontend_infos()

        return context
