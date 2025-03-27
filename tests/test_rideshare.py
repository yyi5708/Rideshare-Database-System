import unittest
from datetime import datetime
from tests.test_data import *
from src.rideshare import *
from src.rideshare_api import *
from src.swen344_db_utils import *
import unittest
from datetime import datetime
from tests.test_data import *
from src.rideshare import *
from src.rideshare_api import *
from src.swen344_db_utils import *

class TestRideShare(unittest.TestCase):

    def test_rebuild_tables(self):

        rebuildTables()
        result = exec_get_all("SELECT * FROM Drivers")
        self.assertEqual([], result, "no rows in Drivers")
        result = exec_get_all("SELECT * FROM Riders")
        self.assertEqual([], result, "no rows in Riders")
        result = exec_get_all("SELECT * FROM Rides")
        self.assertEqual([], result, "no rows in Rides")
        result = exec_get_all("SELECT * FROM RideReviews")
        self.assertEqual([], result, "no rows in RideReviews")
        result = exec_get_all("SELECT * FROM RidePassengers")
        self.assertEqual([], result, "no rows in RidePassengers")

    def test_rebuild_tables_is_idempotent(self):

        rebuildTables()
        rebuildTables()
        result = exec_get_all("SELECT * FROM Drivers")
        self.assertEqual([], result, "no rows in Drivers")
        result = exec_get_all("SELECT * FROM Riders")
        self.assertEqual([], result, "no rows in Riders")
        result = exec_get_all("SELECT * FROM Rides")
        self.assertEqual([], result, "no rows in Rides")
        result = exec_get_all("SELECT * FROM RideReviews")
        self.assertEqual([], result, "no rows in RideReviews")
        result = exec_get_all("SELECT * FROM RidePassengers")
        self.assertEqual([], result, "no rows in RidePassengers")

    def test_seeded_data_without_crashing(self):
        
        rebuildTables()
        result = exec_get_all("SELECT * FROM Drivers")
        self.assertNotEqual([], result, "Drivers data not seeded")
        result = exec_get_all("SELECT * FROM Riders")
        self.assertNotEqual([], result, "Riders data not seeded")
        result = exec_get_all("SELECT * FROM Rides")
        self.assertNotEqual([], result, "Rides data not seeded")
        result = exec_get_all("SELECT * FROM RideReviews")
        self.assertNotEqual([], result, "RideReviews data not seeded")
        result = exec_get_all("SELECT * FROM RidePassengers")
        self.assertNotEqual([], result, "RidePassengers data not seeded")
        
    def test_1_db4(self):
        
        alex_driver_id = create_driver("Alex", "Mazda 6", "123789ABCXYZ", 5.0, "Don’t drive like my brother.", "2024-01-01")
        bobby_driver_id = create_driver("Bobby", "Mazda 6", "123789ABCXYZ", 5.0, "Don’t drive like my brother.", "2024-01-01")
        louie_driver_id = create_driver("Louie", "Mazda 6", "123789ABCXYZ", 5.0, "Don’t drive like my brother.", "2024-01-01")
        elaine_driver_id = create_driver("Elaine", "Mazda 6", "123789ABCXYZ", 5.0, "Don’t drive like my brother.", "2024-01-01")
        tony_driver_id = create_driver("Tony", "Mazda 6", "123789ABCXYZ", 5.0, "Don’t drive like my brother.", "2024-01-01")
        create_ride(alex_driver_id, bobby_driver_id, "Airport", "Home", "Don’t drive like my brother.", "2024-01-01")
        create_ride(alex_driver_id, louie_driver_id, "Airport", "Home", "Don’t drive like my brother.", "2024-01-01")
        create_ride(alex_driver_id, elaine_driver_id, "Airport", "Home", "Don’t drive like my brother.", "2024-01-01")
        create_ride(alex_driver_id, tony_driver_id, "Airport", "Home", "Don’t drive like my brother.", "2024-01-01")
        godot_driver_id = create_driver("Godot", "Toyota Camry", "ABC123", 5.0, "Don’t drive like my brother.", "2024-01-01")
        vladimir_rider_id = create_rider("Vladimir", 5.0, "01234-56789", "2024-01-01")
        create_ride(vladimir_rider_id, godot_driver_id, "Airport", "Home", "Don’t drive like my brother.", "2024-01-01")
        result = get_full_ride_info()
        return result
    
    def test_2_db4(self):
        
        result = get_fare_times()
        return result
        
    # def test_1_db3(self):
        
    #     godot_driver_id = create_driver("Godot", "Toyota Camry", "ABC123", 4.0, "Don’t drive like my brother.", "2024-01-01")
    #     mark_driver_as_available(godot_driver_id)
    #     vladimir_rider_id = create_rider("Vladimir", 4.0, "01234-56789", "2024-01-01")
    #     create_ride(vladimir_rider_id, godot_driver_id, "Rochester, NY", "Syracuse, NY", "Don’t drive like my brother.", "2024-01-01")
    #     vladimir_receipt = get_receipt(vladimir_rider_id, "2024-01-01", "2024-01-02")
    #     godot_receipt = get_receipt(godot_driver_id, "2024-01-01", "2024-01-02")
    #     self.assertIsNone(vladimir_receipt)
    #     self.assertIsNone(godot_receipt)
        
    # def test_2_db3(self):
        
    #     alex_driver_id = create_driver("Alex", "Mazda 6", "123789ABCXYZ", 0.5, "Don’t drive like my brother.", "2024-01-01")
    #     bobby_driver_id = create_driver("Bobby", "Mazda 6", "123789ABCXYZ", 1.5, "Don’t drive like my brother.", "2024-01-01")
    #     louie_driver_id = create_driver("Louie", "Mazda 6", "123789ABCXYZ", 2.5, "Don’t drive like my brother.", "2024-01-01")
    #     elaine_driver_id = create_driver("Elaine", "Mazda 6", "123789ABCXYZ", 3.5, "Don’t drive like my brother.", "2024-01-01")
    #     tony_driver_id = create_driver("Tony", "Mazda 6", "123789ABCXYZ", 4.5, "Don’t drive like my brother.", "2024-01-01")
    #     create_ride(alex_driver_id, bobby_driver_id, "Airport", "Destination", "Don’t drive like my brother.", "2024-01-01")
    #     create_ride(alex_driver_id, louie_driver_id, "Pickup", "Destination", "Don’t drive like my brother.", "2024-01-01")
    #     create_ride(alex_driver_id, elaine_driver_id, "Pickup", "Destination", "Don’t drive like my brother.", "2024-01-01")
    #     create_ride(alex_driver_id, tony_driver_id, "Pickup", "Destination", "Don’t drive like my brother.", "2024-01-01")
    #     create_review(louie_driver_id, "Bad Drive.", "2024-01-01", 2)
    #     create_review(bobby_driver_id, "Good Drive.", "2024-01-01", 5)
    #     create_response(alex_driver_id, louie_driver_id, "Thank You.", "2024-01-01")
    #     alex_receipt = get_receipt(alex_driver_id, "2024-01-01", "2024-01-02")['total_amount']
    #     bobby_receipt = get_receipt(bobby_driver_id, "2024-01-01", "2024-01-02")['total_amount']
    #     louie_receipt = get_receipt(louie_driver_id, "2024-01-01", "2024-01-02")['total_amount']
    #     elaine_receipt = get_receipt(elaine_driver_id, "2024-01-01", "2024-01-02")['total_amount']
    #     tony_receipt = get_receipt(tony_driver_id, "2024-01-01", "2024-01-02")['total_amount']
    #     self.assertEqual(3, alex_receipt)
    #     self.assertEqual(3, bobby_receipt)
    #     self.assertEqual(3, louie_receipt)
    #     self.assertEqual(3, elaine_receipt)
    #     self.assertEqual(3, tony_receipt)

    # def test_3_db3(self):
        
    #     tony_driver_id = create_driver("Tony", "Mazda 6", "123789ABCXYZ", 4.5, "Don’t drive like my brother.", "2024-01-01")
    #     alex_driver_id = create_driver("Alex", "Mazda 6", "123789ABCXYZ", 0.5, "Don’t drive like my brother.", "2024-01-01")
    #     elaine_driver_id = create_driver("Elaine", "Mazda 6", "123789ABCXYZ", 3.5, "Don’t drive like my brother.", "2024-01-01")    
    #     create_ride(tony_driver_id, alex_driver_id, "Start", "Destination", "Don’t drive like my brother.", "2024-01-01")
    #     create_ride(tony_driver_id, elaine_driver_id, "Start", "Destination", "Don’t drive like my brother.", "2024-01-01")
    #     mark_driver_as_unavailable(tony_driver_id)
    #     available_drivers = get_all_drivers_in_zip(None)
    #     self.assertNotIn(tony_driver_id, [driver['driver_id'] for driver in available_drivers])

    # def test_list_rides_given_by_tom(self):

    #     tom_driver_id = create_driver("Tom Magliozzi", "Toyota Camry", "ABC123", 3.2, "Don’t drive like my brother.", "2024-01-01")
    #     ray_driver_id = create_driver("Ray Magliozzi", "Honda Accord", "XYZ789", 3.4, "Don’t drive like my brother.", "2024-01-01")
    #     mike_rider_id = create_rider("Mike Easter", 4.3, "01234-56789", "2024-01-01")
    #     create_ride(tom_driver_id, mike_rider_id)
    #     create_ride(ray_driver_id, mike_rider_id)
    #     create_ride(tom_driver_id, ray_driver_id)
    #     rides = get_rides_given_by_driver(tom_driver_id)
    #     expected_rides = [(tom_driver_id, mike_rider_id), (tom_driver_id, ray_driver_id)]
    #     self.assertCountEqual(expected_rides, rides)

    # def test_list_rides_taken_by_mike(self):

    #     tom_driver_id = create_driver("Tom Magliozzi", "Toyota Camry", "ABC123", 3.2, "Don’t drive like my brother.", "2024-01-01")
    #     ray_driver_id = create_driver("Ray Magliozzi", "Honda Accord", "XYZ789", 3.4, "Don’t drive like my brother.", "2024-01-01")
    #     mike_rider_id = create_rider("Mike Easter", 4.3, "01234-56789", "2024-01-01")
    #     create_ride(tom_driver_id, mike_rider_id)
    #     create_ride(ray_driver_id, mike_rider_id)
    #     create_ride(tom_driver_id, ray_driver_id)
    #     rides = get_rides_taken_by_rider(mike_rider_id)
    #     expected_rides = [(tom_driver_id, mike_rider_id), (ray_driver_id, mike_rider_id)]
    #     self.assertCountEqual(expected_rides, rides)

    # def test_list_rides_given_by_mike(self):

    #     mike_rider_id = create_rider("Mike Easter", 4.3, "01234-56789", "2024-01-01")
    #     rides = get_rides_given_by_driver(mike_rider_id)
    #     self.assertEqual([], rides)

    # def test_tom_checks_his_rating(self):

    #     tom_driver_id = create_driver("Tom Magliozzi", "Toyota Camry", "ABC123", 3.2, "Don’t drive like my brother.", "2024-01-01")
    #     rating = get_rating_by_user(tom_driver_id)
    #     self.assertEqual("3.2", str(rating))

    # def test_ray_checks_his_rating(self):

    #     ray_driver_id = create_driver("Ray Magliozzi", "Honda Accord", "XYZ456", 3.4, "Don’t drive like my brother.", "2024-01-01")
    #     rating = get_rating_by_user(ray_driver_id)
    #     self.assertEqual("3.4", str(rating))
        
    # def test_mike_checks_his_rating(self):

    #     mike_rider_id = create_rider("Mike Easter", 3.6, "01234-56789", "2024-01-01")
    #     rating = get_rating_by_user(mike_rider_id)
    #     self.assertEqual("3.4", str(rating))

    # def test_yousaf_checks_his_rating(self):

    #     yousaf_rider_id = create_rider("Yousaf Iqbal", 3.8, "01234-56789", "2024-01-01")
    #     rating = get_rating_by_user(yousaf_rider_id)
    #     self.assertEqual("3.2", str(rating))

    # def test_tom_and_ray_updated_profiles(self):
        
    #     tom_driver_id = create_driver("Tom Magliozzi", "Toyota Camry", "ABC123", 3.2, "Don’t drive like my brother.", "2024-01-01")
    #     ray_driver_id = create_driver("Ray Magliozzi", "Honda Accord", "XYZ789", 3.4, "Don’t drive like my brother.", "2024-01-01")
    #     update_driver_profile(tom_driver_id, "Toyota Corolla", "123ABC", 3.4, "Don’t drive like my sister.")
    #     update_driver_profile(ray_driver_id, "Honda Civic", "789XYZ", 3.6, "Don’t drive like my sister.")
    #     updated_tom_profile = get_driver_profile(tom_driver_id)
    #     updated_ray_profile = get_driver_profile(ray_driver_id)
    #     self.assertEqual(updated_tom_profile["car_make_model"], "Toyota Corolla")
    #     self.assertEqual(updated_tom_profile["license_number"], "123ABC")
    #     self.assertEqual(updated_tom_profile["average_rating"], 3.4)
    #     self.assertEqual(updated_tom_profile["special_instructions"], "Don’t drive like my sister.")
    #     self.assertEqual(updated_ray_profile["car_make_model"], "Honda Civic")
    #     self.assertEqual(updated_ray_profile["license_number"], "789XYZ")
    #     self.assertEqual(updated_ray_profile["average_rating"], 3.6)
    #     self.assertEqual(updated_ray_profile["special_instructions"], "Don’t drive like my sister.")

    # def test_colburn_and_daisy_signed_up_accounts(self):
        
    #     colburn_driver_id = create_driver("Hoke Colburn", "Nissan Altima", "DEF456", 4.0, "Drive Fast.", "2024-01-01")
    #     daisy_rider_id = create_rider("Ms. Daisy", 3.5, "01234-56789", "2024-01-01")
    #     colburn_profile = get_driver_profile(colburn_driver_id)
    #     daisy_profile = get_rider_profile(daisy_rider_id)
    #     self.assertIsNotNone(colburn_profile)
    #     self.assertIsNotNone(daisy_profile)
    #     self.assertEqual(colburn_profile["name"], "Hoke Colburn")
    #     self.assertEqual(colburn_profile["car_make_model"], "Nissan Altima")
    #     self.assertEqual(colburn_profile["license_number"], "DEF456")
    #     self.assertEqual(colburn_profile["average_rating"], 4.0)
    #     self.assertEqual(colburn_profile["special_instructions"], "Drive Fast.")
    #     self.assertEqual(daisy_profile["name"], "Ms. Daisy")
    #     self.assertEqual(daisy_profile["average_rating"], 3.5)
    #     self.assertEqual(daisy_profile["credit_card_number"], "01234-56789")
    #     self.assertEqual(daisy_profile["joining_date"], "2024-01-01")
        
    # def test_mark_ms_daisy_available(self):
        
    #     daisy_rider_id = create_rider("Ms. Daisy", 3.5, "01234-56789", "2024-01-01")
    #     zip_code = "30301"
    #     time = datetime(2024, 12, 13, 11, 55)
    #     mark_rider_as_available(daisy_rider_id, zip_code)
    #     daisy_profile = get_rider_profile(ms_daisy_rider_id)
    #     self.assertEqual(daisy_profile["is_available"], True)
    #     self.assertEqual(daisy_profile["zip_code"], "30301")
 
    # def test_get_available_fares(self):
        
    #     colburn_driver_id = create_driver("Hoke Colburn", "Nissan Altima", "DEF456", 4.0, "Drive Fast.", "2024-01-01")
    #     daisy_rider_id = create_rider("Ms. Daisy", 3.5, "01234-56789", "2024-01-01")
    #     zip_code = "30301"
    #     mark_rider_as_available(daisy_rider_id, zip_code)
    #     available_fares = get_available_fares(zip_code)
    #     daisy_in_available_fares = False
    #     for fare in available_fares:
    #         if fare["rider_id"] == daisy_rider_id:
    #             daisy_in_available_fares = True
    #             break
    #     self.assertTrue(daisy_in_available_fares)
      
    # def test_get_all_drivers_in_zip(self):
        
    #     colburn_driver_id = create_driver("Hoke Colburn", "Nissan Altima", "DEF456", 4.0, "Drive Fast.", "2024-01-01")
    #     daisy_rider_id = create_rider("Ms. Daisy", 3.5, "01234-56789", "2024-01-01")
    #     zip_code = "30301"
    #     mark_rider_as_available(daisy_rider_id, zip_code)
    #     all_drivers = get_all_drivers_in_zip(zip_code)
    #     colburn_in_drivers = False
    #     for driver in all_drivers:
    #         if driver["driver_id"] == colburn_driver_id:
    #             hoke_colburn_in_drivers = True
    #             break
    #     self.assertTrue(colburn_in_drivers)  
 
    # def test_colburn_drove_daisy(self):
        
    #     colburn_driver_id = create_driver("Hoke Colburn", "Nissan Altima", "DEF456", 4.0, "Drive Fast.", "2024-01-01")
    #     daisy_rider_id = create_rider("Ms. Daisy", 3.5, "01234-56789", "2024-01-01")
    #     zip_code = "30301"
    #     mark_rider_as_available(daisy_rider_id, zip_code)
    #     time = datetime(1989, 12, 13, 12, 0)
    #     create_ride(colburn_driver_id, daisy_rider_id, "Start Point", "Destination", "Drive Fast.", time)
    #     daisy_rides = get_rides_taken_by_rider(daisy_rider_id)
    #     colburn_ride_in_rides = False
    #     for ride in daisy_rides:
    #         if ride["driver_id"] == colburn_driver_id:
    #             colburn_ride_in_rides = True
    #             break
    #     self.assertTrue(colburn_ride_in_rides)
    
    # def test_ride_and_rating(self):
        
    #     colburn_driver_id = create_driver("Hoke Colburn", "Nissan Altima", "DEF456", 4.0, "Drive Fast.", "2024-01-01")
    #     daisy_rider_id = create_rider("Ms. Daisy", 3.5, "01234-56789", "2024-01-01")
    #     zip_code = "30301"
    #     time = datetime(1989, 12, 13, 12, 0)
    #     create_ride(colburn_driver_id, daisy_rider_id, "Start Point", "Destination", "Drive Fast.", time)
    #     ride_id = create_ride(hoke_colburn_id, ms_daisy_id, "Start Point", "Destination", "Drive safely.", time)
    #     colburn_rating = get_rating_by_driver(colburn_driver_id)
    #     self.assertEqual(colburn_rating, 4.0)
    #     daisy_rating = get_rating_by_rider(daisy_rider_id)
    #     self.assertEqual(daisy_rating, 3.5)    

    # def test_tom_drove_colburn(self):
        
    #     tom_driver_id = create_driver("Tom Magliozzi", "Toyota Camry", "ABC123", 3.2, "Don’t drive like my brother.", "2024-01-01")
    #     colburn_rider_id = create_rider("Hoke Colburn", 3.5, "01234-56789", "2024-01-01")  
    #     zip_code = "30301"
    #     mark_rider_as_available(colburn_rider_id, zip_code)
    #     time = datetime(1989, 12, 14, 4, 0)
    #     create_ride(tom_driver_id, colburn_rider_id, "Start Point", "Destination", "Drive Fast.", time)
    #     colburn_rides = get_rides_taken_by_rider(colburn_rider_id)
    #     tom_ride_in_rides = False
    #     for ride in colburn_rides:
    #         if ride["driver_id"] == tom_driver_id:
    #             tom_ride_in_rides = True
    #             break
    #     self.assertTrue(tom_ride_in_rides)
        
    # def test_daisy_removes_account():
        
    #     daisy_rider_id = create_rider("Ms. Daisy", 3.5, "01234-56789", "2024-01-01")
    #     remove_rider_account(daisy_rider_id)
    #     daisy_profile = get_rider_profile(daisy_rider_id)
    #     self.assertIsNone(daisy_profile)