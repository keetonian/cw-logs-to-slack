"""Lambda function handler."""

# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import config
import lambdalogging
from loghelpers import extract_log_events
import slack

LOG = lambdalogging.getLogger(__name__)


def logs_to_slack(event, context):
    """Lambda function handler."""
    LOG.info('Received event: %s', event)
    log_events = extract_log_events(event)
    for log_event in log_events:
        message = log_event['message']
        slack.post_message(config.SLACK_URL, message)
