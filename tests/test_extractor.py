from agent.extractor import MetadataExtractor


def test_extractor():

    extractor = MetadataExtractor()

    result = extractor.extract()

    print()

    for k, v in result.items():
        print(k, ":", v)

    assert result["agreement_number"]