from agent.risk_scanner import RiskScanner


def test_risk_scanner():

    scanner = RiskScanner()

    risks = scanner.scan()

    print()

    for risk in risks:

        print(
            risk["severity"],
            risk["section_number"],
            risk["title"]
        )

    assert len(risks) > 0