import requests


class GoogleMapsAPIService(object):

    def __init__(self):
        self.API_KEY = 'AIzaSyDwZaOYxl4YJov2irWzyHaa45FnHAmH6wQ'
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.params = {}

    def get_data_by_city_name(self, city):
        self.params.update({
            "address": city,
            "key": self.API_KEY
        })
        req = requests.get(self.url, self.params)
        if req.status_code != 200:
            return []
        if req.json().get('status') != "OK" and req.json().get("status") != "ZERO_RESULTS":
            return []
        return req.json()['results']
