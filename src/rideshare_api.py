from src.swen344_db_utils import *

"""
    Function:
        Create a new driver in the database.
    Arguments:
        name (str): The name of the driver.
        car_make_model (str): The make and model of the driver's car.
        license_number (str): The license number of the driver.
        average_rating (float): The initial average rating of the driver.
        special_instructions (str): Special instructions from the driver.
        joining_date (datetime): The date when the driver joined.
    Returns:
        int: The driver_id of the newly created driver.
"""

def create_driver(name, car_make_model, license_number, average_rating, special_instructions, joining_date):
    
    insert_user_sql = """
        INSERT INTO Drivers (name, average_rating, special_instructions, car_make_model, license_number, years_as_driver, joining_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING driver_id
    """
    data_driver = (name, average_rating, special_instructions, car_make_model, license_number, 0, joining_date)
    driver_id = exec_get_one_commit(insert_user_sql, data_driver)
    return driver_id[0]

"""
    Function:
        Create a new rider in the database.
    Arguments:
        name (str): The name of the rider.
        average_rating (float): The initial average rating of the rider.
        credit_card_number (str): The credit card number of the rider.
        joining_date (datetime): The date when the rider joined.
    Returns:
        int: The rider_id of the newly created rider.
"""

def create_rider(name, average_rating, credit_card_number, joining_date):
    
    insert_user_sql = """
        INSERT INTO Riders (name, average_rating, credit_card_number, joining_date)
        VALUES (%s, %s, %s, %s)
        RETURNING rider_id
    """
    data_rider = (name, average_rating, credit_card_number, joining_date)
    rider_id = exec_get_one_commit(insert_user_sql, data_user)
    return rider_id[0]

"""
    Function:
        Create a new ride in the database.
    Arguments:
        driver_id (int): The driver_id of the driver providing the ride.
        rider_id (int): The rider_id of the rider taking the ride.
        start_point (str): The starting point of the ride.
        destination (str): The destination of the ride.
        special_instructions (str): Special instructions for the ride.
        time_info (datetime): The timestamp when the ride takes place.
    Returns:
        int: The ride_id of the newly created ride.
"""

def create_ride(driver_id, rider_id, start_point, destination, special_instructions, time_info):
    
    insert_ride_sql = """
        INSERT INTO Rides (driver_id, rider_id, start_point, destination, special_instructions, time_info)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING ride_id
    """
    data_ride = (driver_id, rider_id, start_point, destination, special_instructions, time_info)
    ride_id = exec_get_one_commit(insert_ride_sql, data_ride)
    return ride_id[0]

"""
    Function:
        Get a list of rides given by a specific driver.
    Arguments:
        driver_id (int): The driver_id of the driver.
    Returns:
        list: A list of dictionaries representing rides given by the driver.
"""

def get_rides_given_by_driver(driver_id):
    
    select_sql = """
        SELECT ride_id, rider_id FROM Rides
        WHERE driver_id = %s
    """
    data = (driver_id,)
    rides = exec_get_all(select_sql, data)
    return rides

"""
    Function:
        Get a list of rides taken by a specific rider.
    Arguments:
        rider_id (int): The rider_id of the rider.
    Returns:
        list: A list of dictionaries representing rides taken by the rider.
"""

def get_rides_taken_by_rider(rider_id):
    
    select_sql = """
        SELECT ride_id, driver_id FROM Rides
        WHERE rider_id = %s
    """
    data = (rider_id,)
    rides = exec_get_all(select_sql, data)
    return rides

"""
    Function:
        Get the average rating of a specific driver.
    Arguments:
        driver_id (int): The driver_id of the driver.
    Returns:
        float: The average rating of the driver.
"""

def get_rating_by_driver(driver_id):
    
    select_sql = """
        SELECT average_rating FROM Drivers
        WHERE driver_id = %s
    """
    data = (driver_id,)
    rating = exec_get_one_commit(select_sql, data)
    return rating[0]

"""
    Function:
        Get the average rating of a specific rider.
    Arguments:
        rider_id (int): The rider_id of the rider.
    Returns:
        float: The average rating of the rider.
"""

def get_rating_by_rider(rider_id):
    
    select_sql = """
        SELECT average_rating FROM Riders
        WHERE rider_id = %s
    """
    data = (rider_id,)
    rating = exec_get_one_commit(select_sql, data)
    return rating[0]

"""
    Function:
        Update the profile of a specific driver.
    Arguments:
        driver_id (int): The driver_id of the driver.
        name (str): The new name of the driver.
        average_rating (float): The new average rating of the driver.
        special_instructions (str): The new special instructions from the driver.
    Returns:
        None
"""

def update_driver_profile(driver_id, name, average_rating, special_instructions):
    
    update_sql = """
        UPDATE Drivers
        SET name = %s, average_rating = %s, special_instructions = %s
        WHERE driver_id = %s
    """
    data = (name, average_rating, special_instructions, driver_id)
    exec_commit(update_sql, data)

"""
    Function:
        Update the profile of a specific rider.
    Arguments:
        rider_id (int): The rider_id of the rider.
        name (str): The new name of the rider.
        average_rating (float): The new average rating of the rider.
        credit_card_number (str): The new credit card number of the rider.
    Returns:
        None
"""

def update_rider_profile(rider_id, name, average_rating, credit_card_number):
    
    update_sql = """
        UPDATE Riders
        SET name = %s, average_rating = %s, credit_card_number = %s
        WHERE rider_id = %s
    """
    data = (name, average_rating, credit_card_number, rider_id)
    exec_commit(update_sql, data)

"""
    Function:
        Remove a specific driver's account from the database.
    Arguments:
        driver_id (int): The driver_id of the driver.
    Returns:
        None
"""

def remove_driver_account(driver_id):
    
    delete_sql = """
        DELETE FROM Drivers
        WHERE driver_id = %s
    """
    data = (driver_id,)
    exec_commit(delete_sql, data)

"""
    Function:
        Remove a specific rider's account from the database.
    Arguments:
        rider_id (int): The rider_id of the rider.
    Returns:
        None
"""

def remove_rider_account(rider_id):
    
    delete_sql = """
        DELETE FROM Riders
        WHERE rider_id = %s
    """
    data = (rider_id,)
    exec_commit(delete_sql, data)

"""
    Function:
        Record a new ride in the database, including reviews.
    Arguments:
        driver_id (int): The driver_id of the driver providing the ride.
        rider_id (int): The rider_id of the rider taking the ride.
        start_point (str): The starting point of the ride.
        destination (str): The destination of the ride.
        special_instructions (str): Special instructions for the ride.
        time_info (datetime): The timestamp when the ride takes place.
    Returns:
        int: The ride_id of the newly created ride.
"""

def record_new_ride(driver_id, rider_id, start_point, destination, special_instructions, time_info):
    
    ride_id = create_ride(driver_id, rider_id, start_point, destination, special_instructions, time_info)
    driver_review_text = "Amazing ride!"
    rider_review_text = "Amazing driver!"
    update_ride_reviews(ride_id, driver_id, driver_review_text)
    update_ride_reviews(ride_id, rider_id, rider_review_text)
    return ride_id

"""
    Function:
        Get a list of available fares/drivers in a specific zip code.
    Arguments:
        zip_code (str): The zip code for which available drivers are queried.
    Returns:
        list: A list of dictionaries representing available drivers.
"""

def get_available_fares(zip_code):
    
    select_sql = """
        SELECT driver_id, coordinates, average_rating
        FROM Drivers
        WHERE zip_code = %s
    """
    data = (zip_code,)
    available_fares = exec_get_all(select_sql, data)
    return available_fares

"""
    Function:
        Get a list of all drivers in a specific zip code.
    Arguments:
        zip_code (str): The zip code for which all drivers are queried.
    Returns:
        list: A list of dictionaries representing all drivers in the zip code.
"""

def get_all_drivers_in_zip(zip_code):
    
    select_sql = """
        SELECT driver_id, coordinates, average_rating
        FROM Drivers
        WHERE zip_code = %s
    """
    data = (zip_code,)
    all_drivers = exec_get_all(select_sql, data)
    return all_drivers

"""
    Function:
        Mark a specific rider as available for rides in a particular zip code.
    Arguments:
        rider_id (int): The rider_id of the rider.
        zip_code (str): The zip code in which the rider is marked as available.
    Returns:
        None
"""

def mark_rider_as_available(rider_id, zip_code):
    
    update_sql = """
        UPDATE Riders
        SET is_available = TRUE, zip_code = %s, coordinates = (SELECT coordinates FROM ZipCodes WHERE zip_code = %s)
        WHERE rider_id = %s
    """
    data = (zip_code, zip_code, rider_id)
    exec_commit(update_sql, data)

"""
    Function:
        Update the location of a specific driver.
    Arguments:
        driver_id (int): The driver_id of the driver whose location is to be updated.
        new_coordinates (str): The new coordinates of the driver.
    Returns:
        None
"""

def update_driver_location(driver_id, new_coordinates):
    
    update_sql = """
        UPDATE Drivers
        SET coordinates = %s
        WHERE driver_id = %s
    """
    data = (new_coordinates, driver_id)
    exec_commit(update_sql, data)

"""
    Function:
        Update the location of a specific rider.
    Arguments:
        rider_id (int): The rider_id of the rider whose location is to be updated.
        new_coordinates (str): The new coordinates of the rider.
    Returns:
        None
"""

def update_rider_location(rider_id, new_coordinates):
    
    update_sql = """
        UPDATE Riders
        SET coordinates = %s
        WHERE rider_id = %s
    """
    data = (new_coordinates, rider_id)
    exec_commit(update_sql, data)

"""
    Function:
        Remove a specific ride from the database.
    Arguments:
        ride_id (int): The ride_id of the ride to be removed.
    Returns:
        None
"""

def remove_ride(ride_id):
    
    delete_sql = """
        DELETE FROM Rides
        WHERE ride_id = %s
    """
    data = (ride_id,)
    exec_commit(delete_sql, data)

"""
    Function:
        Remove all reviews written by a specific user from the database.
    Arguments:
        user_id (int): The user_id of the user whose reviews are to be removed.
    Returns:
        None
"""

def remove_user_reviews(user_id):
    
    delete_sql = """
        DELETE FROM RideReviews
        WHERE reviewer_id = %s
    """
    data = (user_id,)
    exec_commit(delete_sql, data)

"""
    Function:
        Retrieve profile information for a specific driver from the database.
    Arguments:
        driver_id (int): The driver_id of the driver.
    Returns:
        list: A list containing the driver's profile information.
"""

def get_driver_profile(driver_id):

    select_sql = """
        SELECT name, average_rating, special_instructions, car_make_model, license_number, joining_date, coordinates
        FROM Drivers
        WHERE driver_id = %s
    """
    data = (driver_id,)
    profile = exec_get_all(select_sql, data)
    return profile

"""
    Function:
        Retrieve profile information for a specific rider from the database.
    Arguments:
        rider_id (int): The rider_id of the rider.
    Returns:
        list: A list containing the rider's profile information.
"""

def get_rider_profile(rider_id):

    select_sql = """
        SELECT name, average_rating, special_instructions, credit_card_number, joining_date, coordinates, zipcode
        FROM Riders
        WHERE rider_id = %s
    """
    data = (rider_id,)
    profile = exec_get_all(select_sql, data)
    return profile

"""
    Function:
        Mark a driver as available in the database.
    Arguments:
        driver_id (int): The driver_id of the driver.
    Returns:
        None
"""

def mark_driver_as_available(driver_id):
    
    update_sql = """
        UPDATE Drivers
        SET is_available = TRUE
        WHERE driver_id = %s
    """
    data = (driver_id,)
    exec_commit(update_sql, data)

"""
    Function:
        Get the receipt for rides taken by a specific rider within a given time period.
    Arguments:
        rider_id (int): The ID of the rider.
        start_date (datetime): The start date of the time period.
        end_date (datetime): The end date of the time period.
    Returns:
        dict: A dictionary containing the rides taken by the rider and the total amount spent.
"""

def get_receipt(rider_id, start_date, end_date):
    
    select_sql = """
        SELECT *
        FROM Rides
        WHERE rider_id = %s
        AND time_info BETWEEN %s AND %s
    """
    data = (rider_id, start_date, end_date)
    rides = exec_get_all(select_sql, data)
    total_amount = sum(ride['fare'] for ride in rides)
    return {'rides': rides, 'total_amount': total_amount}

"""
    Function:
        Create a review for a ride in the database.
    Arguments:
        ride_id (int): The ID of the ride being reviewed.
        reviewer_id (int): The ID of the user writing the review.
        review_text (str): The text of the review.
        rating (int): The rating given in the review.
    Returns:
        None
"""

def create_review(ride_id, reviewer_id, review_text, rating):
    
    insert_sql = """
        INSERT INTO RideReviews (ride_id, reviewer_id, review_text, rating)
        VALUES (%s, %s, %s, %s)
    """
    data = (ride_id, reviewer_id, review_text, rating)
    exec_commit(insert_sql, data)
    
"""
    Function:
        Create a response to a review in the database.
    Arguments:
        review_id (int): The ID of the review to respond to.
        response_text (str): The text of the response.
        is_driver_response (bool): Indicates whether the response is from the driver or the rider.
    Returns:
        None
"""   

def create_response(review_id, response_text, is_driver_response):
    
    if is_driver_response:
        update_sql = """
            UPDATE RideReviews
            SET driver_response = %s
            WHERE review_id = %s
        """
    else:
        update_sql = """
            UPDATE RideReviews
            SET rider_response = %s
            WHERE review_id = %s
        """
    data = (response_text, review_id)
    exec_commit(update_sql, data)
    
"""
    Function:
        Mark a driver as unavailable in the database.
    Arguments:
        driver_id (int): The ID of the driver to mark as unavailable.
    Returns:
        None
"""      

def mark_driver_as_unavailable(driver_id):
    
    update_sql = """
        UPDATE Drivers
        SET is_available = FALSE
        WHERE driver_id = %s
    """
    data = (driver_id,)
    exec_commit(update_sql, data)

"""
    Function:
        Retrieve full ride information for rides within 1 day of the given date.
    Arguments:
        date (str): The date for which ride information is requested (format: 'YYYY-MM-DD').
    Returns:
        list: A list of dictionaries containing full ride information, including driver name, destination coordinates,
              list of riders, and average rating.
"""

def get_full_ride_info(date):
    select_sql = """
        SELECT driver.name AS driver, ride.destination_lat AS dest_lat, ride.destination_long AS dest_long,
               ARRAY_AGG(rider.name) AS riders, AVG(review.rating) AS avg_rating
        FROM Rides ride
        JOIN Drivers driver ON ride.driver_id = driver.driver_id
        JOIN RideReviews review ON ride.ride_id = review.ride_id
        JOIN Riders rider ON review.reviewer_id = rider.rider_id
        WHERE ride.time_info::date = %s
        GROUP BY ride.ride_id, driver.name, ride.destination_lat, ride.destination_long
    """
    data = (date,)
    ride_info = exec_get_all(select_sql, data)
    return ride_info

"""
    Function:
        Retrieve fare times summary.
    Arguments:
        None
    Returns:
        list: A list of lists containing hour and average fare pairs.
"""

def get_fare_times():
    select_sql = """
        SELECT EXTRACT(HOUR FROM time_info) AS hour, AVG(fare) AS avg_fare
        FROM Rides
        GROUP BY EXTRACT(HOUR FROM time_info)
    """
    fare_times = exec_get_all(select_sql)
    return fare_times