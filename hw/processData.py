
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/zcolley/cs381-MatthewFried/main/hw/cars-sample35.csv', names=['price', 'maintenance_cost', 'number_of_doors', 'number_of_passengers', 'luggage_capacity', 'safety_rating', 'classification_of_vehicle'], header=None)

price = df['price'].tolist()
maintenance_cost = df['maintenance_cost'].tolist()
number_of_doors = df['number_of_doors'].tolist()
number_of_passengers = df['number_of_passengers'].tolist()
luggage_capacity = df['luggage_capacity'].tolist()
safety_rating = df['safety_rating'].tolist()
classification_of_vehicle = df['classification_of_vehicle'].tolist()

# print(df.head(100))
# 3
prince_with_med = [idx for idx, val in enumerate(price) if val == 'med']
# print(prince_with_med)
# 4
passenger_with_price_med = [val for idx, val in enumerate(
    number_of_passengers) if idx in prince_with_med]

print(passenger_with_price_med)
# 5
price_high_with_maintain = [idx for idx, val in enumerate(
    price) if val == 'high' and maintenance_cost[idx] != 'low']
# print(price_high_with_maintain)

# 6
vehicle_rating_med = [val for val in safety_rating if val == 'med']
# print(vehicle_rating_med)

# 7
passenger_with_auto_med = [val for idx, val in enumerate(
    number_of_passengers) if price[idx] == 'med']
print(passenger_with_price_med)


# 8
auto_price_high_with_main_low = price_high_with_maintain = [
    idx for idx, val in enumerate(price) if val == 'high' and maintenance_cost[idx] != 'low']

# print(auto_price_high_with_main_low)


nlist = [[1, 2, 3], ['A', 'B', 'C'], [4, 5, 6], ['D', 'E', 'l']]


new_list = [val for sub in nlist for val in sub]
# print(new_list)
