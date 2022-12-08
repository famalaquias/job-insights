from src.pre_built.sorting import sort_by


job1 = {"min_salary": 100, "max_salary": 1000, "date_posted": '2001-02-01'} 
job2 = {"min_salary": 50, "max_salary": 2000, "date_posted": ''}
job3 = {"min_salary": '', "max_salary": 3000, "date_posted":  '2021-02-01'}
job4 = {"min_salary": 200, "max_salary": '', "date_posted": '2011-02-01'}


MOCK_MAX = [job1, job2, job3, job4]
MOCK_MIN = [job1, job2, job3, job4]
MOCK_DATE = [job1, job2, job3, job4]


def test_sort_by_criteria():
    sort_by(MOCK_MAX, "max_salary")
    assert MOCK_MAX == [job3, job2, job1, job4]
    sort_by(MOCK_MIN, "min_salary")
    assert MOCK_MIN == [job2, job1, job4, job3]
    sort_by(MOCK_DATE, "date_posted")
    assert MOCK_DATE == [job3, job4, job1, job2]
