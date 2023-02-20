from locust import HttpUser, between, task


class DefaultUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def check_response_time(self):
        with self.client.get("/", catch_response=True) as response:
            if response.text != "OK":
                response.failure(
                    f"Wrong response. (status_code={response.status_code})"
                )
