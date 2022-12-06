import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    pass
    assert count_ocurrences("data/jobs.csv", "python") == 1639
    assert count_ocurrences("data/jobs.csv", "PYTHON") == 1639
    assert count_ocurrences("data/jobs.csv", "javascript") == 122
    assert count_ocurrences("data/jobs.csv", "JavaScript") == 122

    with pytest.raises(FileNotFoundError):
        count_ocurrences("data/jobs.json", "python")
