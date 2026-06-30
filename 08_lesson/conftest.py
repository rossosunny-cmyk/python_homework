import os

import pytest

from yougile_api import YougileApi


def get_required_env(name):
    value = os.getenv(name)

    if value is None:
        raise RuntimeError(f"Set {name} environment variable")

    return value


@pytest.fixture()
def api():
    base_url = get_required_env("YOUGILE_BASE_URL")
    token = get_required_env("YOUGILE_TOKEN")

    return YougileApi(base_url, token)


@pytest.fixture()
def user_id():
    return get_required_env("YOUGILE_USER_ID")


@pytest.fixture()
def created_project_ids(api):
    project_ids = []

    yield project_ids

    for project_id in project_ids:
        api.delete_project(project_id)
