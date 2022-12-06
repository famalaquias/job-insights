from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salary = read(path)
    max_salary = []

    for salaries in salary:
        if salaries["max_salary"].isdigit():
            max_salary.append(int(salaries["max_salary"]))
    return max(max_salary)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    salary = read(path)
    min_salary = []

    for salaries in salary:
        if salaries["min_salary"].isdigit():
            min_salary.append(int(salaries["min_salary"]))
    return min(min_salary)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        type(job.get("min_salary")) is not int
        or type(job.get("min_salary")) is not int
        or ("min_salary" or "max_salary") not in job
        or job["min_salary"] > job["max_salary"]
        or isinstance(salary, (int, float, str)) is False
    ):
        raise ValueError

    return job["min_salary"] <= int(salary) <= job["max_salary"]
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    all_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                all_jobs.append(job)
        except ValueError as error:
            print(error)
    return all_jobs

    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
