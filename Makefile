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
		${DOCKER_IMAGE} -m flake8 ./

.PHONY: local-run
local-run: build
	docker run --rm \
		--network=data-foundation_default \
		-e PUBSUB_EMULATOR_HOST=pubsub-emulator:8681 \
		-e GCP_PROJECT_ID=csdf-local-dev \
		-e PUBSUB_TOPIC_NAME=customer-interation-topic \
		${DOCKER_IMAGE}


