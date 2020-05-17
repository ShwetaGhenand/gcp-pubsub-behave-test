# -- FILE: features/example.feature
Feature: Basic pubsub message test

  Scenario: Basic pubsub message test with
    Given valid message json
    When event published onto "pubsub-topic"
    Then the pubsub subscription have received valid messgae 
