import os.path

path = "Settings.txt"

def settingsExist():
      if os.path.isfile(path):
          print("Found Settings\n")
      else:
        file = open(path,"w")
        file.write("theme = System\n" 
                   "motivationsites =\n"
                   "productivesites =\n")
        file.close

def convertTodictionary():
    settingsExist()
    websitesMotive = list("")
    websitesProtive = list("")
    settingsDict= {
'theme': "",
'motivationsites': "",
'productivesites': ""
}
    file = open(path, "r")
    #TODO add logic of productive websites to the dictionary
    for line in file:
        if not line.startswith("motive") and not line.startswith ("protive"):
            key = line[0:line.find(" ")]
            keyValue = line[line.index("=") + 1: line.find("\n")]
            settingsDict.update({key:(settingsDict.get(key) + keyValue).strip()})
        elif line.startswith("motive"):
            websitesMotive.append(line.index(line.index(":"), line.__sizeof__))
        elif line.startswith("protive"):
            websitesProtive.append(line.index(line.index(":"), line.__sizeof__))
    file.close
    return settingsDict
