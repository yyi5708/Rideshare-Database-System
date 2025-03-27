import unittest
import csv
from datetime import datetime
from src.rideshare import *
from src.rideshare_api import *
from src.swen344_db_utils import *
import unittest
import csv
from datetime import datetime
from src.rideshare import *
from src.rideshare_api import *
from src.swen344_db_utils import *

def test_data():
    
    tom_driver_id = create_driver("Tom Magliozzi", "Toyota Camry", "ABC123", 3.2, "Don’t drive like my brother.", "2024-01-01")
    ray_driver_id = create_driver("Ray Magliozzi", "Honda Accord", "XYZ789", 3.4, "Don’t drive like my brother.", "2024-01-01")
    mike_rider_id = create_rider("Mike Easter", 4.3, "01234-56789", "2024-01-01")
    create_ride(tom_driver_id, mike_rider_id)
    create_ride(ray_driver_id, mike_rider_id)
    create_ride(tom_driver_id, ray_driver_id)
    alex_driver_id = create_driver("Alex", "Mazda 6", "123789ABCXYZ", 0.5, "Don’t drive like my brother.", "2024-01-01")
    bobby_driver_id = create_driver("Bobby", "Mazda 6", "123789ABCXYZ", 1.5, "Don’t drive like my brother.", "2024-01-01")
    louie_driver_id = create_driver("Louie", "Mazda 6", "123789ABCXYZ", 2.5, "Don’t drive like my brother.", "2024-01-01")
    elaine_driver_id = create_driver("Elaine", "Mazda 6", "123789ABCXYZ", 3.5, "Don’t drive like my brother.", "2024-01-01")
    tony_driver_id = create_driver("Tony", "Mazda 6", "123789ABCXYZ", 4.5, "Don’t drive like my brother.", "2024-01-01")
    csv_file = 'rideshare.csv'
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            joining_date_str = row['joiningDate']
            joining_date = datetime.strptime(joining_date_str, '%m/%d/%Y').date()
            if row['riderordriver'] == 'driver':
                car_make_model = "Nissan Altima"
                license_number = 'ABCXYZ123789'
                average_rating = 3.6
                special_instructions = 'Don’t drive like my brother.'
                create_driver(name, car_make_model, license_number, average_rating, special_instructions, joining_date)
            elif row['riderordriver'] == 'rider':
                average_rating = 4.6
                credit_card_number = '98765-43210'
                create_rider(name, average_rating, credit_card_number, joining_date)