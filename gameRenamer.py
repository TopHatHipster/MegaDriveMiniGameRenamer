import os

directory = os.path.dirname("gameRenamer.py")
print("Beware!\nMega Drive/Genesis games with a .SMD file extension\nmay be incompatible with\nthe Mega Drive/Genesis Mini systems!\nThey will be renamed to .bin files as well with this application,\nso make sure to remove the .SMD games before starting the bulk renaming.")
dirname = input("\n\nWhat is the folder (in this very own folder)\ncalled where you stored your Mega Drive/Genesis games?\n")

gameDirectory = os.path.join(directory, dirname)
gameList = os.listdir(gameDirectory)

gameNumber = 0
for game in gameList:
    gameName = gameList[gameNumber]
    gameName = gameName.split('.')
    newName = gameName[0] + ".bin"
    os.rename((os.getcwd() + "/" + dirname + "/" + gameName[0]+ "." + gameName[1]), os.getcwd() + "/" + dirname + "/"  + (gameName[0]+ ".bin"))
    print(newName)
    gameNumber += 1

input("Games renamed! Press any key to exit.")
