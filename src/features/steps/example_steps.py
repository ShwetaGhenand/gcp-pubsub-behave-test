import json

# -- FILE: features/steps/example_steps.py
from behave import given, when, then
from main import Main


@given('valid message json')
def given_step_impl(context):
    context.main = Main()
    context.messgae = context.main.read_json('/src/features/fixtures/publish_message.json')


@when('event published onto "pubsub-topic"')
def when_step_impl(context):
    message_id = context.main.publish_message(context.messgae)
    assert message_id is not None


@then(u'the pubsub subscription have received valid messgae')
def then_step_impl(context):
    expected_received_messgae = context.main.read_json('/src/features/fixtures/receive_message.json')
    actual_recieved_event = context.main.read_message(context.main.pubsub_topic_subscription_path)

    for actual_received_message in actual_recieved_event:
        assert expected_received_messgae['attributes'] == actual_received_message.message.attributes
        assert expected_received_messgae['data'] == json.loads(actual_received_message.message.data)
