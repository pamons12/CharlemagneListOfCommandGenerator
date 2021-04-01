import requests
from bs4 import BeautifulSoup

resultFile = open("result.txt","w")

def main():
    htmlFile = "serverOverView.html"

    websiteList = goThroughFile(htmlFile)

    ironBannerCommandList = []
    trialsCommandList = []
    raidCommandList = []
    gambitCommandList = []
    doublesCommandList = []
    d1CommandList = []

    for website in websiteList:
        webPage = requests.get(website).content
        soup = BeautifulSoup(webPage,'html.parser')

        soupResult = soup.html.findAll("code")

        if (len(soupResult)>0):
            command = str(soupResult[0])[6:-7]
        
        soupResult = soup.html.findAll(class_="m-b-xs")
        if (len(soupResult)>0):
            description = str(soupResult[0])[39:-6]

        if ("D1" in description.upper()):
            d1CommandList.append(command + " -> " + description)
        elif ("IB" in description.upper() or "IRON BANNER" in description.upper()):
            ironBannerCommandList.append(command + " -> " + description)
        elif ("TRIALS" in description.upper()):
            trialsCommandList.append(command + " -> " + description)
        elif ("DOUBLE" in description.upper()):
            doublesCommandList.append(command + " -> " + description)
        elif ("RAID" in description.upper() or"LEV" in command.upper() or "EOW" in command.upper() or "SOS" in command.upper() or "SOTP" in command.upper() or "COS" in command.upper() or "LAST WISH" in description.upper() or "GOS" in command.upper() or "DSC" in command.upper()):
            raidCommandList.append(command + " -> " + description)
        elif ("GAMBIT" in description.upper()):
            gambitCommandList.append(command + " -> " + description)
        else:
            resultFile.write(command + " -> " + description + "\n")
    
    writeListToFile(d1CommandList,"Destiny 1 Commands")
    writeListToFile(ironBannerCommandList,"Iron Banner Commands")
    writeListToFile(trialsCommandList,"Trials Commands")
    writeListToFile(doublesCommandList,"Double PVP Commands")
    writeListToFile(raidCommandList,"Raid Commands")
    writeListToFile(gambitCommandList,"Gambit Commands")

    resultFile.close()
    print("Done")


def goThroughFile(inFileName):
    inFile = open(inFileName,"r")
    websites=[]

    for line in inFile:
        temp = line.split('"')
        if len(temp)>2:
            websites.append("https://warmind.io"+temp[1])
    return websites

def writeListToFile(writeList,category):
    resultFile.write("\n********** "+category+" **********\n")
    for command in writeList:
        resultFile.write(command + "\n")

main()