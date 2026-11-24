# SPDX-FileCopyrightText: 2026 Germán Rocha
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert right ascension and declination to altitude and azimuth."""

import math
from datetime import datetime, timezone

def find_object_by_id(id):
    celestial_objects = [
        {"id": 1, "name": "Saturn", "ra_hours": 19, "declination_degrees": 12.9},
        {"id": 2, "name": "Jupiter", "ra_hours": 19, "declination_degrees": 12.9},
        {"id": 3, "name": "Vega", "ra_hours": 19, "ra_degrees": 279.234735, "declination_degrees": 38.78},
        {"id": 4, "name": "Polaris", "ra_hours": 19, "declination_degrees": 12.9},
        {"id": 5, "name": "Proxima Centauri", "ra_hours": 19, "declination_degrees": 12.9},
    ]

    for celestial_object in celestial_objects:
        if celestial_object["id"] == id:
            return celestial_object

    return None


reference_time = datetime(2000, 1, 1, 12, 0, tzinfo=timezone.utc)

print ("\t\t\t\t\tCOORDINATES CALCULATOR\n\n")
print ("Please select one of the following stars or planets:\n")
print ("1. Saturn\n2. Jupiter\n3. Vega\n4. Polaris\n5. Proxima Centauri\n")

object_number = int(input("Enter the option: "))
selected_object = find_object_by_id(object_number)

print (f"Your selected option was: {object_number} - {selected_object["name"]}\n\n")

latitude_deg = float(input ("Enter your latitude (positive for north, negative for south: \n"))
longitude_deg = float(input ("Enter your longitude (positive for west, negative for east: \n"))

time_input = input ("Enter the time (YYYY-MM-DD HH:MM:SS): ")

observation_time_utc = datetime.fromisoformat(time_input.strip()).astimezone(timezone.utc)
elapsed = observation_time_utc - reference_time

d = elapsed.total_seconds() / 86_400

print (f"d = {d}")

local_sidereal_angle_deg = (280.46061837 + (360.98564736629 * d) + longitude_deg) % 360

print (f"local sidereal angle: {local_sidereal_angle_deg}")

local_sidereal_time = local_sidereal_angle_deg / 15

print (f"local sidereal time: {local_sidereal_time}")

hour_angle_deg = local_sidereal_angle_deg - selected_object["ra_degrees"]

print (f"hour angle deg: {hour_angle_deg}")

east_component = (-math.cos(math.radians(selected_object["declination_degrees"]))) * math.sin(math.radians(hour_angle_deg))

print (f"east component: {east_component}")

north_component = (math.cos(math.radians(latitude_deg)) * math.sin(math.radians(selected_object["declination_degrees"]))) - (math.sin(math.radians(latitude_deg)) * math.cos(math.radians(selected_object["declination_degrees"])) * math.cos(math.radians(hour_angle_deg)))

print (f"north component: {north_component}")

up_component = (math.sin(math.radians(latitude_deg)) * math.sin(math.radians(selected_object["declination_degrees"]))) + (math.cos(math.radians(latitude_deg)) * math.cos(math.radians(selected_object["declination_degrees"])) * math.cos(math.radians(hour_angle_deg)))

print (f"up component: {up_component}")

print ("--------------------------------------------")

altitude_deg = math.degrees(math.asin(up_component))

print (f"\n\nALTITUDE: {altitude_deg}")

azimuth_deg = (math.degrees(math.atan2(east_component, north_component)) + 360) % 360

print (f"AZIMUTH: {azimuth_deg}")


