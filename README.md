# Puppy Lambda

This mini-project provides an AWS Lambda that creates a JSON document from a specific endpoint and uploads it to a S3 bucket.

## Prerequisites

- This project was developed with Python 3.7+

## Getting Started

- git clone & cd into it
- Make the virtual environment:
  - `mkvirtualenv -p /usr/local/bin/python3.8 -r requirements.txt`

### Tests

- coming eventually
- In the meantime, lint with `flake8`

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of `~/.aws/credentials`. To use another profile, append something like `--profile user1`.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control.

## Invocation

	lambda invoke -v
 
## Deploy
    
To deploy:

	lambda deploy --requirements requirements.txt
