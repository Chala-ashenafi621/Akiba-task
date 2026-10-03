# TASK 7 — Travel Planner
destination = input("Destination: ")
distance = float(input("Distance in kilometers: "))
average_speed = float(input("Average speed in km/h: "))
travel_time = distance / average_speed
travel_minutes=travel_time*60
print("\n================================")
print("        TRAVEL PLANNER            ")
print("===================================")

print("Destination:", destination)
print("Distance:", distance, "km")
print("Average Speed:", average_speed, "km/h")
print("Estimated Travel Time:", travel_time, "hours")
print("Estimated Travel minutes:",travel_minutes,"minutes")

print("================================")
