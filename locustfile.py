from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before 
            any task is scheduled
        """
        self.login()

    def login(self):
        self.client.post("/login",
                         {"username":"ellen",
                          "password":"education"})

    @task
    def index(self):
        self.client.get("/")

    @task
    def profile(self):
        self.client.get("/profile")

class WebsiteUser(HttpLocust):
    host = "https://google.com"
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000