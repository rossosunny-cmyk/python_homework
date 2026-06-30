from uuid import uuid4

from yougile_api import YougileApi


def get_project_title():
    return f"Autotest project {uuid4().hex}"


def create_test_project(api, created_project_ids, user_id):
    title = get_project_title()
    response = api.create_project(title, user_id)

    assert response.status_code == 201

    project_id = response.json()["id"]
    created_project_ids.append(project_id)

    return project_id, title


def assert_error_response(response):
    assert response.status_code >= 400
    assert YougileApi.get_error_message(response) != ""


def test_create_project_positive(api, created_project_ids, user_id):
    title = get_project_title()
    response = api.create_project(title, user_id)

    assert response.status_code == 201

    project_id = response.json()["id"]
    created_project_ids.append(project_id)

    assert project_id != ""


def test_create_project_negative(api, user_id):
    response = api.create_project_without_title(user_id)

    assert_error_response(response)


def test_get_project_positive(api, created_project_ids, user_id):
    project_id, title = create_test_project(
        api,
        created_project_ids,
        user_id,
    )

    response = api.get_project(project_id)

    assert response.status_code == 200

    project = response.json()

    assert project["id"] == project_id
    assert project["title"] == title


def test_get_project_negative(api):
    project_id = uuid4().hex

    response = api.get_project(project_id)

    assert_error_response(response)


def test_update_project_positive(api, created_project_ids, user_id):
    project_id, _ = create_test_project(
        api,
        created_project_ids,
        user_id,
    )
    new_title = get_project_title()

    response = api.update_project(project_id, {"title": new_title})

    assert response.status_code == 200

    get_response = api.get_project(project_id)
    project = get_response.json()

    assert get_response.status_code == 200
    assert project["id"] == project_id
    assert project["title"] == new_title


def test_update_project_negative(api):
    project_id = uuid4().hex

    response = api.update_project(project_id, {"title": get_project_title()})

    assert_error_response(response)
