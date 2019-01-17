import pytest
import myfunction


def test_handler(mocker):
    myfunction.handler({}, None)
