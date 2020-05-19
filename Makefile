DOCKER_IMAGE = pubsub-behave-test

.PHONY: all
all:

.PHONY: clean
clean:

.PHONY: build
build:
	@echo "Docker Build..."
	docker build -t $(DOCKER_IMAGE) .

.PHONY: lint
lint: build
	docker run --rm \
	    --entrypoint python3 \
		${DOCKER_IMAGE} -m flake8 ./

.PHONY: local-run
local-run: build
	docker-compose up 
