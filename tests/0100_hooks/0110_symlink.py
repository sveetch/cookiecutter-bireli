import os
from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def symlink_structure(tmp_path):
    """
    Create a basic structure where to work in: ::

    ├── foo/
    │   └── bar/
    │       └── foobar.txt
    └── ping/
        ├── existing/
        └── pong/
    """
    foo = tmp_path / "foo"
    bar = foo / "bar"
    ping = tmp_path / "ping"
    pong = ping / "pong"
    existing = ping / "existing"
    foobar = bar / "foobar.txt"
    bar.mkdir(parents=True)
    pong.mkdir(parents=True)
    existing.mkdir(parents=True)
    foobar.write_text("Ping! Pong!")

    return tmp_path


def test_symlink_sources_to_subdir_file(symlink_structure, postgen_manager):
    """
    Check for symlink to a file in a subdirectory
    """
    manager = postgen_manager(symlink_structure)
    created = manager.symlink_sources([
        ("foo/bar/foobar.txt", "new-target"),
    ])

    expected = symlink_structure / "new-target"

    assert created == [
        ("new-target", "foo/bar/foobar.txt"),
    ]
    assert expected.exists() is True
    assert expected.is_file() is True
    assert expected.is_symlink() is True


def test_symlink_sources_to_aside_file(symlink_structure, postgen_manager):
    """
    Check for symlink to a file in the same directory
    """
    manager = postgen_manager(symlink_structure)
    created = manager.symlink_sources([
        ("foo/bar/foobar.txt", "foo/bar/new-target"),
    ])

    expected = symlink_structure / "foo/bar/new-target"

    assert created == [
        ("foo/bar/new-target", "foobar.txt"),
    ]
    assert expected.exists() is True
    assert expected.is_file() is True
    assert expected.is_symlink() is True


def test_symlink_sources_to_outside_file(symlink_structure, postgen_manager):
    """
    Check for symlink to a file in a parent directory different than the symlink one
    """
    manager = postgen_manager(symlink_structure)
    created = manager.symlink_sources([
        ("foo/bar/foobar.txt", "ping/new-target"),
    ])

    expected = symlink_structure / "ping/new-target"

    assert created == [
        ("ping/new-target", "../foo/bar/foobar.txt"),
    ]
    assert expected.exists() is True
    assert expected.is_file() is True
    assert expected.is_symlink() is True


def test_symlink_sources_to_outside_directory(symlink_structure, postgen_manager):
    """
    Check for symlink to a directory in a parent directory different than the symlink
    one
    """
    manager = postgen_manager(symlink_structure)
    created = manager.symlink_sources([
        ("foo/bar", "ping/pong/new-target"),
    ])

    expected = symlink_structure / "ping/pong/new-target"

    assert created == [
        ("ping/pong/new-target", "../../foo/bar"),
    ]
    assert expected.exists() is True
    assert expected.is_dir() is True
    assert expected.is_symlink() is True


def test_symlink_sources_overwrite_to_directory(symlink_structure, postgen_manager):
    """
    Check for symlink to a file in a parent directory different than the symlink
    one and the symlink will overwrite an existing directory.
    """
    manager = postgen_manager(symlink_structure)
    created = manager.symlink_sources([
        ("foo/bar", "ping/existing"),
    ])

    expected = symlink_structure / "ping/existing"

    assert created == [
        ("ping/existing", "../foo/bar"),
    ]
    assert expected.exists() is True
    assert expected.is_dir() is True
    assert expected.is_symlink() is True


def test_symlink_sources_overwrite_to_file(symlink_structure, postgen_manager):
    """
    Check for symlink to a directory in a parent directory different than the symlink
    one and the symlink will overwrite an existing directory.
    """
    manager = postgen_manager(symlink_structure)
    created = manager.symlink_sources([
        ("foo/bar/foobar.txt", "ping/existing"),
    ])

    expected = symlink_structure / "ping/existing"

    assert created == [
        ("ping/existing", "../foo/bar/foobar.txt"),
    ]
    assert expected.exists() is True
    assert expected.is_file() is True
    assert expected.is_symlink() is True


def test_symlink_sources_invalid_missing_source(symlink_structure, postgen_manager):
    """
    Method should raise exception when source path does not exists.
    """
    manager = postgen_manager(symlink_structure)

    with pytest.raises(ValueError) as excinfo:
        manager.symlink_sources([
            ("nope.txt", "invalid"),
        ])

    assert str(excinfo.value) == (
        "Given source path does not exists: {}".format(symlink_structure / "nope.txt")
    )


def test_symlink_sources_invalid_same_paths(symlink_structure, postgen_manager):
    """
    Method should raise exception when source path and destination path resolve to the
    same path.
    """
    manager = postgen_manager(symlink_structure)

    with pytest.raises(ValueError) as excinfo:
        manager.symlink_sources([
            ("foo/bar/foobar.txt", "nope/niet"),
        ])

    assert str(excinfo.value) == (
        "Given destination path belong to a parent directory that does not exists: "
        "{}".format(symlink_structure / "nope/niet")
    )
