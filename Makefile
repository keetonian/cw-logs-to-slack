SHELL := /bin/sh
PY_VERSION := 3.7

# Required environment variables (user must override)

# S3 bucket used for packaging SAM templates
PACKAGE_BUCKET ?= your-bucket-here

# user can optionally override the following by setting environment variables with the same names before running make

# Path to system pip
PIP ?= pip
# Default AWS CLI region
AWS_DEFAULT_REGION ?= us-east-1
STACK_NAME ?= cw-logs-to-slack
SLACK_URL ?= https://slack.com
LOG_GROUP_NAME ?= name
FILTER_PATTERN ?= error

PYTHON := $(shell /usr/bin/which python$(PY_VERSION))

.DEFAULT_GOAL := lint
.PHONY: test clean undeploy deploy package compile build publish bootstrap init

# used once just after project creation to lock and install dependencies
bootstrap:
	$(PYTHON) -m $(PIP) install pipenv --user
	pipenv lock
	pipenv sync --dev

# used by CI build to install dependencies
init:
	$(PYTHON) -m $(PIP) install pipenv --user
	pipenv sync --dev

lint:
	pipenv run cfn-lint template.yml

deploy: lint
	pipenv run sam deploy --template-file template.yml --stack-name $(STACK_NAME) --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND --parameter-overrides SlackUrl=${SLACK_URL} LogGroupName=${LOG_GROUP_NAME} FilterPattern=${FILTER_PATTERN}

# used to delete the cfn stack
undeploy:
	pipenv run aws cloudformation delete-stack --stack-name $(STACK_NAME)

publish: package
	pipenv run sam publish --template template.yml
