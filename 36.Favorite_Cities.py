# Favorite Cities 🌆

🔽 class City:
🔽   def __init__(self, name, country, population, landmarks):
       self.name = name
       self.country = country
       self.population = population
       self.landmarks = landmarks

nyc = City("New York City", "USA", 8468000, ["Statue of Liberty", "Brooklyn Bridge", "Apollo Theatre"])
shangai = City("Shangai", "China", "26320000, ["The Bund", "Jin Mao Tower", "Tianzifang"])

print(vars(nyc))
print(vars(shangai))