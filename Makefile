GIT_HASH ?= $(shell git log --format="%h" -n 1)
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

build:
		docker build . --tag ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH}
 
push:
		docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH}

start:
		docker-compose up

release:
		docker tag  ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH} ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest
		docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest
