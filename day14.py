dir = "UDLLRRDDRULU"

countU = dir.count("U")
countD = dir.count("D")
countL = dir.count("L")
countR = dir.count("R")

if countU == countD and countL == countR:
     print(True)
else:
     print(False)