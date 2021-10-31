class CharacterSheet:
  def __init__(self, attack, defense, luck, items):
    self.attack = attack
    self.defense = defense
    self.luck = luck
    self.items = items
  
  def sheet(givenRace, givenClass):
    if givenRace == "human":
      attack = 5
      defense = 5
      luck = 5
    
    if givenClass == "knight":
      items = ["sword", "shield"]
    
    characterSheet = {
    "Attack": attack,
    "Defense": defense,
    "Luck": luck,
    "Items": items
    }

    return characterSheet