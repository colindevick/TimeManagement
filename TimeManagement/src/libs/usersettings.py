import os.path

path = "Settings.txt"

def settingsExist():
      if os.path.isfile(path):
          print("Found Settings\n")
      else:
        file = open(path,"x")
        file.write("theme = System\n" 
                   "motivationsites =\n"
                   "productivesites =\n")
        file.close

def convertTodictionary():
    settingsExist()
    websitesMotive = list("")
    websitesProtive = list("")
    settingsDict= {
"theme": "",
"motivationwebsites": "",
"productivesites": ""
}
    file = open(path, "r")
    #TODO add logic of productive websites to the dictionary
    for line in file:
        if not line.startswith("motive") and not line.startswith ("protive"):
            key = line.slice[0:line.find(" ")]
            value = line.split.rslice[0: line.find("=")]
            settingsDict.update({key: settingsDict.get(key)})
        elif line.startswith("motive"):
            websitesMotive.append(line.index(line.index(":"), line.__sizeof__))
        elif line.startswith("protive"):
            websitesProtive.append(line.index(line.index(":"), line.__sizeof__))
    return settingsDict