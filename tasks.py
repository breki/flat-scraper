# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=import-error

import platform

# noinspection PyUnresolvedReferences
from invoke import task


@task
def blackd(c):
    """
    Run black daemon.

    """
    _poetry_run(c, "blackd")


@task
def mypy(c):
    """
    Run MyPy on the project code.

    """
    _poetry_run(c, "run-mypy")


@task
def lint(c):
    """
    Run linting tools.

    """
    _poetry_run(c, "run-lint")


@task
def radon_maintainability(c):
    """
    Run Radon analysis of code maintainability.

    """
    _poetry_run(c, "run-radon-maintainability")


@task
def radon_complexity(c):
    """
    Run Radon analysis of code complexity.

    """
    _poketry_run(c, "run-radon-complexity")


@task(radon_maintainability, radon_complexity)
def code_complexity(_):
    """
    Run all Radon analyses.
    """


@task(name="py-install")
def py_install(c):
    """
    Synchronize the Python virtual environment based on the Poetry lock file\
 (or create the virtual environment if none exists).
    """
    _poetry(c, "install")


@task(name="py-upgrade")
def py_upgrade(c):
    """
    Upgrade the Python virtual environment packages according to the\
 pyproject.toml file.
    """
    _poetry(c, "update")


@task(
    name="build",
    pre=[lint, mypy, code_complexity],
)
def build(_):
    """
    Run the complete local development build.
    """


@task(help={"cmd": "Poetry command to run."})
def poetry(c, cmd):
    """
    Execute the specified Poetry command.

    """
    _poetry(c, cmd)


def _poetry_run(c, command: str):
    _poetry(c, "run " + command)


def _poetry(c, command: str):
    print("")
    print(f"Running:")
    print(f"poetry {command}")
    print("")

    with c.cd("src/django/waga"):
        c.run("poetry " + command)


def _on_windows():
    return platform.system() == "Windows"
