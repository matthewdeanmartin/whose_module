import whose_module._version


def test_import_it():
    # lamest, first test.
    import whose_module

    dir(whose_module)
    assert whose_module._version.__version__

    import whose_module.__main__

    dir(whose_module.__main__)
