from agent.graph import contract_agent


def test_graph():

    response = contract_agent.invoke(
        {
            "query": "Can either party terminate for convenience?"
        }
    )

    print()
    print(response["response"])

    assert response["response"]