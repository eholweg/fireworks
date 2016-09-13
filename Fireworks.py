import re
import datetime
from subprocess import call

# EJHOLWEG

class Fireworks:

    # def makeFWM(fd):
    #     return "FCST," + fd['id'] + "," + fd['date'] + "," + fd['hr'] + "," + fd['wx'] + "," + fd['temp'] + "," + \
    #            fd['rh'] + "," + fd['lal1423'] + "," + fd['lal2323'] + "," + fd['wdir'] + "," + fd['wspd'] + "," + \
    #            fd['tenhr'] + "," + fd['maxtemp'] + "," + fd['mintemp'] + "," + fd['maxrh'] + "," + fd['minrh'] + \
    #            "," + fd['pd1305'] + "," + fd['pd0513'] + "," + fd['wetflag'] + fd['fcstAdds']

    @property
    def main(self):
        FWMWRK = "./data/FWMWRK"
        FWOMRX = "./data/FWOMRX"
        FIREWORKS = "./data/FIREWORKS"

        dtg=datetime.datetime.utcnow()
        zdate=dtg.strftime("%d%H%M")

        FIREWORK="FNUS84 KMRX "+zdate+"\nFWMWRK\n\n"

        obPattern = re.compile('\D+\s+\d{6}\s\d{6}.*')
        fcstPattern=re.compile('FCST,.*')

        fullObsDict={}
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
                #print fcst

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
                           "wetflag": fcstList[18],
                           "fcstLine": fcst.rstrip(),
                           "fcstAdds": ''
                           }
                fullFcstDict[fcstList[1]] = fcstDict

        #for k in fullFcstDict:
            #print k, fullFcstDict[k]['maxtemp']

        for k in fullObsDict:
            if fullFcstDict[k]['sta_id'] == k:
                #check if fcst max temp < obs dbt+2
                tempThresh = int( fullFcstDict[k]['maxtemp'] ) - int( fullObsDict[k]['dbt'] )
                #print "FC MAX TEMP--> ",fullFcstDict[k]['maxtemp']
                #print "OB TEMP--> ", fullObsDict[k]['dbt']
                if abs(tempThresh) < 3:
                    fullFcstDict[k]['fcstAdds']+=" [OB TEMP="+fullObsDict[k]['dbt']+"]\n"
                    fullFcstDict[k]['maxtemp']="["+fullFcstDict[k]['maxtemp']+"]"
                else:
                    fullFcstDict[k]['fcstAdds'] += "\n"


            fd=fullFcstDict[k]
            FIREWORK+="FCST," + fd['sta_id'] + "," + fd['date'] + "," + fd['hr'] + "," + fd['wx'] + "," + \
              fd['temp'] + "," + fd['rh'] + "," + fd['lal1423'] + "," + fd['lal2323'] + "," + \
              fd['wdir'] + "," + fd['wspd'] + "," + fd['tenhr'] + "," + fd['maxtemp'] + "," + \
              fd['mintemp'] + "," + fd['maxrh'] + "," + fd['minrh'] + "," + fd['pd1305'] + \
              "," + fd['pd0513'] + "," + fd['wetflag'] + fd['fcstAdds']

            output=open(FIREWORKS, 'w')
            output.write(FIREWORK)
            output.close()
                #print  fullFcstDict[k]['fcstLine']
                #print fullFcstDict[k]['sta_id'], fullObsDict[k]




Fireworks().main