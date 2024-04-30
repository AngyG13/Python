# Pokédex 📟

# class definition
🔽 class Pokemon:
🔽   del __init__(self, entry, name, types, description, level, region, is_caught):
         self.entry = entry
         self.name = name
         self.types = types
         self.description + description
         self.level = level
         self.region = region
         self.is_caught = is_caught
        
    def speak(self):
       print("self.name + ". " + self.name +"!")
    def display_details(self):
       print("Entry number: "+ str(self.entry))
       print("Name: " + self.name)
    if len(self.types == 1:
     print("Type: " + self.types[0])
    else:
     print("Type: " + stelf.types[0] + "/" + self. types[1])
    
    print('lv. ' + str(self.level))
    print('Region: ' + self. region)
    print('Description: ' + self.description)
    
    if self.is_caught:
       print(self.name + " has already been caught!")
    else:
       print(self.name + " hasn\'s been caught yet.")
    
# Pokemon objects
pikachu = pokemon(25, "Pikachu", ["Electric"], "It has small electric sacs on both its cheek. If threatened, it looses electric charges from the sacs.", 25, "Kanto", True)
charizard = pokemon(3, "Charizard", ["Fire", "Flying"], "It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.", 36,"Kanto" False)
gyarados = pokemos(130, "Gyarados", ["Water", "Flying"], "It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.", 57, "Kanto", False)

pikachu.speak()
charizard.speak()
gyarados.speak()