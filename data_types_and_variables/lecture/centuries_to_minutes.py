centuries = int(input())
to_years = 100 * centuries
to_days = int(to_years * 365.2422)
to_hours = int(to_days * 24)
to_minutes = int(to_hours * 60)

print(f"{centuries} centuries = {to_years} years = {to_days} days = {to_hours} hours = {to_minutes} minutes")

