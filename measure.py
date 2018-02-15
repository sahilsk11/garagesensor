#/usr/bin/python

#Author Sahil Kapur


import sensor

def get_distance():
    dm = sensor.initialize_sensor()
    dist = sensor.measure_distance(dm)
    return dist

def check_garage_status(dist, open_threshold, car_threshold, closed_threshold):
    if (dist <= open_threshold + 5 and dist >= open_treshold - 5):
        return "open"
    else if (dist >= open_threshold and dist >= car_threshold - 5 and dist <= car_threshold + 5):
        return "closed_car"
    else if (dist >= car_threshold and dist >= open_threshold - 5 and dist >= open_threshold + 5):
        return "closed_car"
    return "error - distance = " + dist  