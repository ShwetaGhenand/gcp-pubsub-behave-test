import json
import os
import time
from google.api_core import exceptions
from google.cloud import pubsub_v1


class Main:

    def __init__(self):
        self.project_id = os.environ['GCP_PROJECT_ID']
        self.pubsub_topic_name = os.environ['PUBSUB_TOPIC_NAME']
        self.pubsub_topic_subscription_path = self.create_pubsub_subscription(self.pubsub_topic_name)

    def read_json(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            data = json.load(f)
        return data

    def publish_message(self, data):
        publisher = pubsub_v1.PublisherClient()
        topic_path = self.init_pubsub_topic(self.pubsub_topic_name)
        payload = json.dumps(data['data']).encode('utf-8')
        future = publisher.publish(
            topic_path, payload, **data['attributes']
        )
        message_id = future.result()
        return message_id

    def create_pubsub_subscription(self, topic_name):
        subscriber = pubsub_v1.SubscriberClient()
        topic_path = self.init_pubsub_topic(topic_name)
        subscription_name = '{}-default-subscription'.format(topic_name)
        subscription_path = subscriber.subscription_path(
            self.project_id, subscription_name
        )
        try:
            subscriber.create_subscription(
                subscription_path, topic_path
            )
        except exceptions.AlreadyExists:
            pass
        return subscription_path

    def read_message(self, subscription_path):
        subscriber = pubsub_v1.SubscriberClient()
        NUM_MESSAGES = 1
        response = subscriber.pull(subscription_path, max_messages=NUM_MESSAGES)
        ack_ids = []
        for received_message in response.received_messages:
            ack_ids.append(received_message.ack_id)
        if len(ack_ids) != 0:
            subscriber.acknowledge(subscription_path, ack_ids)
            subscriber.close()
        return response.received_messages

    def init_pubsub_topic(self, topic_name):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project_id, topic_name)
        try:
            publisher.get_topic(topic_path)
        except exceptions.NotFound:
            retry_delay = 1
            print(f'Topic path: {topic_path} not found!, retrying in {retry_delay} seconds...')
            time.sleep(retry_delay)
            self.init_pubsub_topic(topic_name)
        return topic_path
