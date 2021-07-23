from datetime import date 
dte = date.today()
todayNum = dte.strftime("%j") # the day of the year today
todayWk = dte.strftime("%w") # the day of the week today
monthSum = [0,31,59,90,120,151,181,212,243,273,304,334]
leapList = [2024,2028,2032,2036,2040,2044,2048,2052,2056,2060, \
    2060,2064,2068,2072,2076,2080,2084,2088,2092,2096, \
    2104,2108,2112,2116,2120,2124,2128,2132,2136,\
    2140,2144,2148,2152,2156,2160,2164,2168,2172,2176,2180,\
    2184,2188,2192,2196,2204,2208,2212,2216,2220,2224,2228, \
    2232,2236,2240,2244,2248,2252,2256,2260,2264,2268,2272,2276, \
    2280,2284,2288,2292,2296,2304,2308,2312,2316,2320,2324,2328,2332, \
    2336,2340,2344,2348,2352,2356,2360,2364,2368,2372,2376,2380,2384]
if dte.year in leapList:
    monthSum = [0,31,60,91,121,152,182,213,244,274,305,335]
bdMonth = int(input("In what month were you born? For January input 1, for February input 2 ... for December input 12:  "))
bdDay = int(input("On what day of the month were you born? (e.g.: 3, 18, 21):  "))
bdNum = bdDay + monthSum[bdMonth-1] # the day of the year of the birthday

def dayDiff(todayNum, bdNum) -> int: # function to get weekday difference
    diff = (int(bdNum) - int(todayNum))%7
    return diff

dayDict = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
lookup = int(todayWk) + dayDiff(todayNum, bdNum)
if lookup > 6:
  lookup -= 7
print("Your birthday will be on a " + dayDict[lookup] + " this year!")
