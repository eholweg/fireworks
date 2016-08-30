import re
import string

class Fireworks:

    def main(self):
        FWMWRK = "./data/FWMWRK"
        FWOMRX = "./data/FWOMRX"
        FWMMRX = "./data/FWMMRX"

        obPattern = re.compile('\D+\s+\d{6}\s\d{6}.*')
        fcstPattern=re.compile('FCST,.*')

        fullObsDict={}
        obsDict={};

        #READ IN THE OBS FILE
        f = open(FWOMRX, 'r')
        fwo = f.readlines()

        for ob in fwo:
            matchOb=re.match(obPattern, ob)
            if matchOb:
                #print "MATCH -- "+ob.rstrip()
                obList=string.split(ob.rstrip());

                obsDict={"sta_name": obList[0],
                         "date": obList[2],
                         "hr": obList[3],
                         "t": obList[4],
                         "w": obList[5],
                         "dbt": obList[6],
                         "dpt": obList[7],
                         "rh": obList[8],
                         "y": obList[9],
                         "m": obList[10],
                         "dir": obList[11],
                         "ws": obList[12],
                         "10": obList[13],
                         "tmx": obList[14],
                         "tmn": obList[15],
                         "hmx": obList[16],
                         "hmn": obList[17],
                         "pd1": obList[18],
                         "pd2": obList[19]
                         }
                fullObsDict[obList[1]]=obsDict
                #print obList[1]

        #NOW READ IN THE WRKFCST FILE
        fm = open(FWMWRK, 'r')
        fwm = fm.readlines()

        for fcst in fwm:
            matchOb = re.match(fcstPattern, fcst)
            if matchOb:
                # print "MATCH -- "+ob.rstrip()
                obList = string.split(ob.rstrip());

                obsDict = {"sta_name": obList[0],
                           "date": obList[2],
                           "hr": obList[3],
                           "t": obList[4],
                           "w": obList[5],
                           "dbt": obList[6],
                           "dpt": obList[7],
                           "rh": obList[8],
                           "y": obList[9],
                           "m": obList[10],
                           "dir": obList[11],
                           "ws": obList[12],
                           "10": obList[13],
                           "tmx": obList[14],
                           "tmn": obList[15],
                           "hmx": obList[16],
                           "hmn": obList[17],
                           "pd1": obList[18],
                           "pd2": obList[19]
                           }
                fullObsDict[obList[1]] = obsDict

        for k in fullObsDict:
            print k, fullObsDict[k]['tmx']



Fireworks().main()