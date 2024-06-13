# Define Hotel Cost by multiplying the number of night by the pay rate
def hotel_cost(num_nights):
    price_per_night = 50
    return num_nights * price_per_night

# Define Car Cost by multiplying the number of night by the pay rate
def car_cost(rental_days):
        daily_price = 30
        return rental_days * daily_price

# Define Plane Cost to identify city costs, the examples given are different costs
def plane_cost(city):
      # Creating a dictionary to map city costs
      city_costs = {
            "london" : 500,
            "berlin" : 600, 
            "tokyo" : 750,
            "new york" : 800
                        }
    
      # Check if city is in the dictionary, if not, return none
      return city_costs.get(city_lower)
    
# Define Holiday Cost by adding all different costs together
def holiday_cost(num_nights, rental_days, city):
     hotelCost = hotel_cost(num_nights)
     planeCost = plane_cost(city)
     carCost = car_cost(rental_days)
     # check if planeCost is None, this indicates an invalid city input
     if planeCost is None:
          return None
     total_cost = hotelCost + planeCost + carCost
     return total_cost

# User inputs the city they will fly to
while True:
     city = input("Enter the city you will be flying to (E.g. london, tokyo, berlin, new york): ")
     # Convert city input to lowercase for case-insensitive comparison
     city_lower = city.lower()
     # Check if city input is valid, if not, a displya error appears
     if plane_cost(city.lower) is not None:
           break
     else:
           print("Eror: Invalid city entered. please enter a valid city.")

# user inputs number of nights they are staying 
num_nights = int(input("Enter the number of nights you are staying at the hotel: "))

# user inputs number of days they rented a car
rental_days = int(input("Enter the number of days you will rent a car: "))

# Calculate total holiday cost
total_cost = holiday_cost(num_nights, rental_days, city)

# Print the total cost for the holiday if it is valid, otherwise print error message
if total_cost is not None:
     print(f"The total cost for {num_nights} nights in the city {city}, When the car is rented for {rental_days} days is £{total_cost}.")
else:
      print("Eror: Invalid city entered. please enter a valid city.")