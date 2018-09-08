# AnyMind small project


## About

An application that contains two endpoint for tweeter search:
- `api/hashtag/<hashtag>` - returns tweets search result for the hashtag.
- `api/users/<username>` - returns tweets search result for certain user.

Optional parameter is `pages_size`, it is limit number of returned data in the
case it is lower than default number of tweets.

Tweet data are scrub from the html page (Tweet API is not used) that is why maximum length of the received data doesn't exceed 20 tweets.


## Containers list

Project contains the only one container with the application.

## Getting started

### Deployment

Deployment is based on the `Docker` containers. There is the config file
`docker-compose.yml` for local deployment.

Docker and Docker Compose are required to be installed before start
the deploying.

Clone project.

Local deployment can be started by the docker-compose up command in the
console:

    docker-compose up

  Note: Development server available on `localhost:8001`


### Running tests

* to run tests locally:
    install the `tox` by `pip install tox` and run command:

        > tox

 `tox` runs flake8 linter tests and pytest environment, each of them could be
 started separately by the commands:

        > tox -e flake8
        > tox -e pytests
