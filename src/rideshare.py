from src.swen344_db_utils import *

def rebuildTables():
    
    conn = connect()
    cur = conn.cursor() 
    drop_sql = """
        DROP TABLE IF EXISTS RideReviews;
        DROP TABLE IF EXISTS Rides;
        DROP TABLE IF EXISTS RidePassengers;
        DROP TABLE IF EXISTS Riders;
        DROP TABLE IF EXISTS Drivers;
    """
    create_sql = """
        CREATE TABLE Drivers (
	    driver_id SERIAL PRIMARY KEY,
  	    name TEXT NOT NULL,
  	    average_rating DECIMAL(2,1) NOT NULL,
  	    special_instructions TEXT,
        car_make_model TEXT NOT NULL,
        license_number TEXT NOT NULL,
        years_as_driver INTEGER NOT NULL,
        joining_date TIMESTAMP NOT NULL,
        coordinates POINT,
        is_available BOOLEAN DEFAULT TRUE );

        CREATE TABLE Riders (
	    rider_id SERIAL PRIMARY KEY,
  	    name TEXT NOT NULL,
  	    average_rating DECIMAL(2,1) NOT NULL,
  	    special_instructions TEXT,
  	    credit_card_number TEXT,
        joining_date TIMESTAMP NOT NULL,
        coordinates POINT,
        zipcode TEXT,
        is_available BOOLEAN DEFAULT TRUE );

        CREATE TABLE Rides (
  	    ride_id SERIAL PRIMARY KEY,
  	    driver_id INTEGER NOT NULL REFERENCES Drivers(driver_id),
	    rider_id INTEGER NOT NULL REFERENCES Riders(rider_id),
        start_point TEXT NOT NULL,
        destination TEXT NOT NULL,
        special_instructions TEXT,
        time_info TIMESTAMP NOT NULL,
        driver_review_text TEXT,
        rider_review_text TEXT,
        fare TEXT );
        
        CREATE TABLE RideReviews (
        review_id SERIAL PRIMARY KEY,
        ride_id INTEGER NOT NULL REFERENCES Rides(ride_id),
        reviewer_id INTEGER NOT NULL REFERENCES Riders(rider_id),
        review_text TEXT,
        driver_response TEXT,
        rider_response TEXT );
        
        CREATE TABLE RidePassengers (
        ride_id INTEGER NOT NULL REFERENCES Rides(ride_id),
        passenger_id INTEGER NOT NULL REFERENCES Riders(rider_id),
        PRIMARY KEY (ride_id, passenger_id) );
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)
    conn.commit()
    conn.close()