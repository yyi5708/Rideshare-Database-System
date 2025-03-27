# Future Plans

## Surge Pricing
If surge pricing were to be added to the system, several changes would be necessary:

### Tables Changes:
1. **Fares Table:** Addition of columns to store surge pricing information, such as surge multiplier and surge start/end times.

### API Methods:
1. **Update Fare:** This method would allow administrators to update fare information, including surge pricing details.
2. **Get Fare Details:** This method would provide detailed fare information, including surge pricing data.

### Existing API Methods Changes:
1. **Create Ride:** This method might need to incorporate surge pricing information to calculate the fare.
2. **Get Available Fares:** Surge pricing data would need to be considered while listing available fares.

## Future Scheduling
For enabling future scheduling in the system, the following changes would be required:

### Tables Changes:
1. **Rides Table:** Addition of columns to store scheduled ride information, such as scheduled time.
2. **Drivers Table:** Addition of columns to track drivers' availability for scheduled rides.

### API Methods:
1. **Schedule Ride:** This method would allow users to schedule rides for a future date and time.
2. **Update Ride Status:** This method would enable users to modify or cancel scheduled rides.

### Existing API Methods Changes:
1. **Get Available Fares:** This method might need to consider scheduled rides when listing available fares.
2. **Get Ride Details:** Additional details about scheduled rides might need to be included in the response.