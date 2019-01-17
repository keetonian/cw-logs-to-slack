import pytest
import handlers
import requests
import responses
import slack

import test_constants


def test_interact_with_slack(mocker):
    handlers.interact_with_slack({}, None)


def test_logs_to_slack(mocker):
    mocker.patch.object(slack, 'post_message')
    handlers.logs_to_slack(test_constants.AWS_LOG_EVENT, None)
    slack.post_message.assert_any_call(test_constants.SLACK_URL, test_constants.EXTRACTED_LOG_EVENTS[0]['message'])
    slack.post_message.assert_any_call(test_constants.SLACK_URL, test_constants.EXTRACTED_LOG_EVENTS[1]['message'])
