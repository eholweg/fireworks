import re
import string

# EJHOLWEG

class Fireworks:

    def main(self):
        FWMWRK = "./data/FWMWRK"
        FWOMRX = "./data/FWOMRX"
        FWMMRX = "./data/FWMMRX"

        obPattern = re.compile('\D+\s+\d{6}\s\d{6}.*')
        fcstPattern=re.compile('FCST,.*')

        fullObsDict={}
        #obsDict={}
        fullFcstDict={}

        #READ IN THE OBS FILE
        f = open(FWOMRX, 'r')
        fwo = f.readlines()

        for ob in fwo:
            matchOb=re.match(obPattern, ob)
            if matchOb:
                #print "MATCH -- "+ob.rstrip()
                obList=ob.rstrip().split()

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
            matchFcst = re.match(fcstPattern, fcst)
            if matchFcst:
                print fcst

                fcstList = fcst.rstrip().split(',')

                fcstDict = {"sta_id": fcstList[1],
                           "date": fcstList[2],
                           "hr": fcstList[3],
                           "wx": fcstList[4],
                           "temp": fcstList[5],
                           "rh": fcstList[6],
                           "lal1423": fcstList[7],
                           "lal2323": fcstList[8],
                           "wdir": fcstList[9],
                           "wspd": fcstList[10],
                           "tenhr": fcstList[11],
                           "maxtemp": fcstList[12],
                           "mintemp": fcstList[13],
                           "maxrh": fcstList[14],
                           "minrh": fcstList[15],
                           "pd1305": fcstList[16],
                           "pd0513": fcstList[17],
                           "wetflag": fcstList[18]
                           }
                fullFcstDict[fcstList[1]] = fcstDict

        for k in fullFcstDict:
            print k, fullFcstDict[k]['maxtemp']



Fireworks().main()