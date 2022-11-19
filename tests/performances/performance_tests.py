from locust import HttpUser, task


class PerfTest(HttpUser):
    club_name = "She Lifts"
    club_email = "kate@shelifts.co.uk"
    competition_name = "Spring Festival"
    book_places = 0


    def on_start(self):
        self.client.get("/")
        self.client.post(
            "/showSummary",
            data={
                "email": self.club_email
            })


    @task
    def test_book(self):
        url = f"/book/{self.competition_name}/{self.club_name}"
        self.client.get(url, name="/book")

    @task
    def test_purchase(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": self.book_places,
                "club": self.club_name,
                "competition": self.competition_name
            })

    @task
    def test_dashboard(self):
        self.client.get("/dashboard")