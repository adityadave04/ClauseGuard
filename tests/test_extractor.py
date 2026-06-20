from agent.extractor import ContractExtractor


def test_extractor():

    extractor = ContractExtractor()

    result = extractor.extract()

    print()

    for k, v in result.items():
        print(k, ":", v)

    assert result["agreement_number"]