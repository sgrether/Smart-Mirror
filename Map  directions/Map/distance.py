#Abstract: distance.py  using Google's geolocation python package with their Distance Matrix API
#can call list of all origins and destinations some wants to travel and give them the time and distance it takes to either drive or bicycle to that given location.
#Author: Michael Royal
#Date:12/11/16
# -*- coding: utf-8 -*-
from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

if __name__ == "__main__":
    origins = ['Monterey', 'Pacific Grove']
    destinations = ['Seaside']
     #API key
    google_maps = GoogleMaps(api_key='AIzaSyBTfMBsYy9fFaJ-XVhoHIz-VnKiN2DZGpg')

    items = google_maps.distance(origins, destinations).all()  # default mode parameter is const.MODE_DRIVING
    #list of items for origin and destination for driving
    for item in items:
        print('Driving origin: %s' % item.origin)
        print('Driving destination: %s' % item.destination)
#       print('km: %s' % item.distance.kilometers)
#       print('m: %s' % item.distance.meters)
#       print('miles: %s' % item.distance.miles)
        print('Average travel duration: %s \n' % item.duration)  # it returns str
#       print('Average duration datetime: %s \n' % item.duration.datetime)  # it returns datetime
    #list of items for origin and destination for driving
    items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_BICYCLING).all()

    for item in items:
        print('Bicycling origin: %s' % item.origin)
        print('Bicycling destination: %s' % item.destination)
#       print('km: %s' % item.distance.kilometers)
#       print('m: %s' % item.distance.meters)
#       print('miles: %s' % item.distance.miles.format(round(item,2)))
        print('Average travel duration: %s \n' % item.duration)
