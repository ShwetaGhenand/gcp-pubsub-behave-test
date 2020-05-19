# gcp-pubsub-behave-test

Test GCP PubSub Behaviour ushing pubsub emulator and behave in python.  Behavioural tests are a tool to formalize the application functionality requirements into tests. 

To show you just how simple a behave test, create a new file called example-feature with the following: 

```
# -- FILE: features/example.feature
Feature: Basic pubsub message test

  Scenario: Basic pubsub message test with
    Given valid message json
    When event published onto "pubsub-topic"
    Then the pubsub subscription have received valid messgae 

```

In this test, we'll send a message to pubsub topic and verify the subscriber receives the valid message. This works by subscribing to the topic specified before running the when and then waiting for that message to be received.

Now to see how Behave works, simply open a terminal in the root directory of your code and run the following command:

```
    make local-run
```

You should see this output:

```
  When event published onto "pubsub-topic"                 # features/steps/example_steps.py:13
  Then the pubsub subscription have received valid messgae # features/steps/example_steps.py:18
  
 1 feature passed, 0 failed, 0 skipped
 1 scenario passed, 0 failed, 0 skipped
 3 steps passed, 0 failed, 0 skipped, 0 undefined
 Took 0m1.378s

```



