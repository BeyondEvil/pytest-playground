.ONESHELL:
SHELL := /bin/bash

.PHONY: start stop enter

start:
	@printf "BROWSER=$(browser)\nPYTHON_VERSION=${py-version}\n" > .env
	docker-compose up -d

stop:
	@docker-compose down

enter:
	@docker exec -ti runner /bin/bash
