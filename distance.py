from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

def dist():
    origin = ['Santa Cruz']
    destination = ['Seaside']
    duration = []

    google_maps = GoogleMaps(api_key='AIzaSyBTfMBsYy9fFaJ-XVhoHIz-VnKiN2DZGpg')

    items = google_maps.distance(origin, destination).all()

    for item in items:
        duration.append('Travel Time: %s' % item.duration)

    return duration
