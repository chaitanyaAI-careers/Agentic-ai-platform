from showcase.evaluation.evaluation_example import EvaluationCase, evaluate


def test_evaluation_summary():
    summary = evaluate(
        [
            EvaluationCase(expected="approved", actual="APPROVED"),
            EvaluationCase(expected="blocked", actual="blocked"),
            EvaluationCase(expected="passed", actual="failed"),
        ]
    )

    assert summary.total == 3
    assert summary.passed == 2
    assert round(summary.pass_rate, 2) == 0.67
