import requests


class YougileApi:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, title, user_id):
        payload = {
            "title": title,
            "users": {
                user_id: "admin",
            },
        }
        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers,
        )

    def create_project_without_title(self, user_id):
        payload = {
            "users": {
                user_id: "admin",
            },
        }
        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers,
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
        )

    def update_project(self, project_id, payload):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers,
        )

    def delete_project(self, project_id):
        return self.update_project(project_id, {"deleted": True})

    @staticmethod
    def get_error_message(response):
        try:
            data = response.json()
        except ValueError:
            return response.text

        if "message" in data:
            return str(data["message"])

        if "error" in data:
            return str(data["error"])

        return str(data)
