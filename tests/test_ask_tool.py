from agent.tools import AskTool


def test_ask_tool():

    tool = AskTool()

    result = tool.ask(
        "Can either party terminate for convenience?"
    )

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")

    for source in result["sources"]:
        print(
            source["section_number"],
            source["section_title"]
        )

    assert result["answer"]