from src.pre_built.sorting import sort_by


jobOne = {"min_salary": 100, "max_salary": 1000, "date_posted": "2000-11-19"}
jobTwo = {"min_salary": "", "max_salary": 3000, "date_posted": "2000-11-19"}
jobThree = {"min_salary": 300, "max_salary": "", "date_posted": "2000-11-19"}
jobFour = {"min_salary": 500, "max_salary": 5000, "date_posted": ""}


MOCK_MAX = [jobOne, jobTwo, jobThree, jobFour]
MOCK_MIN = [jobOne, jobTwo, jobThree, jobFour]
MOCK_DATE = [jobOne, jobTwo, jobThree, jobFour]


def test_sort_by_criteria():
    pass
    sort_by(MOCK_MAX, "max_salary")
    assert MOCK_MAX == [jobTwo, jobThree, jobOne, jobFour]
    sort_by(MOCK_MIN, "min_salary")
    assert MOCK_MIN == [jobThree, jobOne, jobFour, jobTwo]
    sort_by(MOCK_DATE, "date_posted")
    assert MOCK_DATE == [jobTwo, jobFour, jobOne, jobThree]
