import requests


class GoogleMapsAPIService(object):

    def __init__(self):
        self.API_KEY = 'AIzaSyDwZaOYxl4YJov2irWzyHaa45FnHAmH6wQ'
        self.url = 'https://www.googleapis.com/geolocation/v1/geocode/json'
        self.params = {}

    def get_data_by_city_name(self, city):
        self.params.update({
            "address": city,
            "key": self.API_KEY
        })
        req = requests.get(self.url, self.params)
        if req.status_code != 200:
            return []
        return req.json()['results']
