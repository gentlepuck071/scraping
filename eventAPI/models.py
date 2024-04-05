from django.db import models


class EventUrl(models.Model):
    type = models.CharField(max_length=20)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url


class City(models.Model):
    city_href = models.CharField(max_length=20)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Web3event(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    source_url = models.CharField(max_length=100)
    # event_url = models.CharField(max_length=100)
    # summary = models.CharField(max_length=300)
    # description = models.CharField()
    organizer = models.CharField(max_length=50)
    # start_time = models.CharField(max_length=20)
    # end_time = models.CharField(max_length=20)
    # time_zone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
