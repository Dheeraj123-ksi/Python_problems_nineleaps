
# Inputs
total_distance_km = 10000 # total distance to be covered
avg_speed_kmph = 10    # average speed in km/h
hours_per_day = 6     # hours Sandeep cycles per day
# Calculations
total_hours = total_distance_km / avg_speed_kmph
total_days = total_hours / hours_per_day
years = int(total_days // 365)
remaining_days = total_days % 365
months = int(remaining_days // 30)
days = int(remaining_days % 30)
hours = int((remaining_days % 1) * 24)
# Output
print(f"Time required: {years} years, {months} months, {days} days, {hours} hours")