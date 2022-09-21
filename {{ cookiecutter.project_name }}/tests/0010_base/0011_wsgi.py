def test_ensure_wsgi_importable():
    import project.wsgi  # noqa: F401
