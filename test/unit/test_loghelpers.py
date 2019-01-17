import pytest
import loghelpers
import test_constants


def test_extract_log_events(mocker):
    log_events = loghelpers.extract_log_events(test_constants.AWS_LOG_EVENT)
    assert log_events == test_constants.EXTRACTED_LOG_EVENTS