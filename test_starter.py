from starter import Starter


def test_pass():
    result = Starter().entrypoint()
    assert result is True


def test_fail():
    result = Starter().entrypoint()
    assert result is False
