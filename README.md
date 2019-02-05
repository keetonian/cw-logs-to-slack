# cw-logs-to-slack

This serverless app publishes AWS CloudWatch logs to Slack based on a subscription filter.

## App Architecture

![App Architecture](https://github.com/keetonian/cw-logs-to-slack/raw/master/images/cw-logs-to-slack.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:289559741701:applications~cw-logs-to-slack) and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

### Slack Url
To get a webhook URL for this application:
* Navigate to https://api.slack.com
* Click on the "Start Building" button
* Give your app a name and select a workspace
* Under "Add features and functionality" select "Incoming Webhooks"
* Turn on "Incoming Webhooks" and click "Add New Webhook to Workspace"
* Select the desired channel and click "Authorize"
* Copy the generated Webhook URL

### Log Group Name
You can find the name of the log group by navigating to CloudWatch logs on the AWS console. You can also pass it in as a parameter from another stack or another resource (e.g. default lambda log group names are `/aws/lambda/{lambda-function-name}`).

### Filter Pattern
CloudWatch logs allow you to filter logs based on a pattern. For more information, see the [AWS Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

## App Parameters

1. `SlackUrl` (required) - Webhook URL for integration with Slack
1. `LogGroupName` (required) - Log group to listen to (has to be in same account and region)
1. `FilterPattern` (optional) - Pattern for filtering log events. Default: ERROR
1. `OnlySendLogMessage` (optional) - Option to only send log message instead of all message, id, and timestamp information. Default: False. Values: False, True
1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO

## App Outputs

1. `LogsToLambdaName` - Log Lambda Function Name
1. `LogsToLambdaArn` - Log Lambda Function ARN
1. `LambdaToSlackName` - Slack Lambda Function Name
1. `LambdaToSlackArn` - Slack Lambda Function ARN

## License Summary

This code is made available under the MIT license. See the LICENSE file.

## Releases

If you would like to see a version of this application that uses code instead of other applications, see the [0.0.1 Release](https://github.com/keetonian/cw-logs-to-slack/tree/0.0.1).
