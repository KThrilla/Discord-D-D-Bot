import discord
import os
import time
from CharacterSheet import CharacterSheet
#from keep_alive import keep_alive

client = discord.Client()

playerList = []
refrenceList = []
runGame = True
dungeonMaster = ""

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #Start of Message Handler
  if message.author == client.user:
    return
    
####### Dungeon Master Methods ##############################
  async def helpDungeonMaster():
    await message.channel.send("Dungeon Master Commands:\n$help - look up commands\n$add player - add a player mid-game\n$delete player - remove a player from the game\n$skip - skip a player's turn\n$event - allows players to do what they want\n$fight # [name of enemy] - make as many enemies fight the players\n$end - ends the game")
  
  async def addPlayers():
    msg = await client.wait_for('message')

    for player in msg.content.split(" "):
      playerList.append(player)

  async def deletePlayers():
    msg = await client.wait_for('message')

    for player in msg.content.split(" "):
      playerList.remove(player)
  
  async def skipPlayer():
    return #TODO
  
  async def eventTurn():
    return #TODO

  async def endGame():
    await message.channel.send("Dungeon Master Ended The Game")
    quit()


  ####### Player Methods ####################################
  async def helpPlayer():
    await message.channel.send("Dungeon Master Commands:\n$help - look up commands\n$attack - attacks enemy\n$defend - Reduces incoming damage\n$run - run away from a fight\n$sheet - look at your character sheet")

  async def attack():
    return #TODO

  async def defend():
    return #TODO

  async def run():
    return #TODO

  async def characterSheet(player, givenRace, givenClass):
    sheet = CharacterSheet.sheet(givenRace, givenClass)

    refrence = str(player) + "'s Character Sheet\n" + str(givenRace) + " " + str(givenClass) + "\n" + str(sheet)
    
    refrenceList.append(player)
    refrenceList.append(refrence)
    await message.channel.send(refrence)
  
  async def initializePlayer(player):
    await message.channel.send(str(player) + " choose your Race and Class:\nRaces:Human, Orc, Elf, Goblin, Demon\nClasses: Knight, Archer, Mage, Theif, Cook, Doctor")
    msg = await client.wait_for('message')
    stringSplit = msg.content.split(" ")
    await characterSheet(player, stringSplit[0], stringSplit[1])
  

####### Start Of The Game ##############################
  if ('<@!904149165318238261>' in message.content or '<@904149165318238261>' in message.content) and message.channel.name == 'bot-stuff' and len(playerList) == 0:
    dungeonMaster = message.author.name
    await message.channel.send(str(dungeonMaster) + "is Dungeon Master \nMention the Players")

    time.sleep(1)
    await addPlayers()
    await message.channel.send("Players: " + str(playerList))

    for player in playerList:
      await initializePlayer(player)

####### Run Game Loop Start ##############################
  while runGame:
    msg = await client.wait_for('message')

    ########## If Statements for Dungeon Master ############################
    if msg.author.name == dungeonMaster and msg.content.startswith("$help"):
      await helpDungeonMaster()
      
    if msg.author.name == dungeonMaster and msg.content.startswith("$add player"):
      await addPlayers()
      await message.channel.send("Players: " + str(playerList))
    
    if msg.author.name == dungeonMaster and msg.content.startswith("$delete player"):
      await deletePlayers()
      await message.channel.send("Players: " + str(playerList))
    
    if msg.author.name == dungeonMaster and msg.content.startswith("$skip"):
      await skipPlayer()
    
    if msg.author.name == dungeonMaster and msg.content.startswith("$event"):
      await eventTurn()

    if msg.author.name == dungeonMaster and msg.content.startswith("$end"):
      await endGame()
    
    ########## If Statements for Dungeon Master ############################
    if msg.author.name == dungeonMaster and msg.content.startswith("$end"):
      await endGame()
    

    #while(runGame):
      



#keep_alive()
client.run(os.environ['BotToken'])