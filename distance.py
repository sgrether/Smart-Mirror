# -*- coding: utf-8 -*-
from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

if __name__ == "__main__":
    origins = ['San Jose', 'Santa Cruz']
    destinations = ['Seaside']

    google_maps = GoogleMaps(api_key='AIzaSyBTfMBsYy9fFaJ-XVhoHIz-VnKiN2DZGpg')

    items = google_maps.distance(origins, destinations).all()  # default mode parameter is const.MODE_DRIVING

    for item in items:
        print('Driving origin: %s' % item.origin)
        print('Driving destination: %s' % item.destination)
#       print('km: %s' % item.distance.kilometers)
#       print('m: %s' % item.distance.meters)
#       print('miles: %s' % item.distance.miles)
        print('Average travel duration: %s \n' % item.duration)  # it returns str
#       print('Average duration datetime: %s \n' % item.duration.datetime)  # it returns datetime

    items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_BICYCLING).all()

    for item in items:
        print('Bicycling origin: %s' % item.origin)
        print('Bicycling destination: %s' % item.destination)
#       print('km: %s' % item.distance.kilometers)
#       print('m: %s' % item.distance.meters)
#       print('miles: %s' % item.distance.miles.format(round(item,2)))
        print('Average travel duration: %s \n' % item.duration)
