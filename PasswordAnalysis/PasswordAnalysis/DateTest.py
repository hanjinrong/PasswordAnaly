# -*- coding: utf-8 -*-

import re
import datetime

def where_is_year(str):
    if len(str)==8:
        #yyyymmdd
        if 1900<int(str[0:4])<2016:
            if(0<int(str[4:6])<13):
                if(0<int(str[6:])<32):
                    return 1
            #ddmmyyyy
        elif 1900<int(str[4:])<2016:
            if(0<int(str[2:4])<13):
                if(0<int(str[0:2])<32):
                    return 1
                #mmddyyyy
            elif(0<int(str[2:4])<32):
                if(0<int(str[0:2])<13):
                    return 1
    elif len(str)==6:
        #yymmdd
        if 0<int(str[0:2])<100:
            if 0<int(str[2:4])<13:
                if 0<int(str[4:])<32:
                    return 1
        #mmddyy
        elif 0<int(str[4:])<100:
            if 0<int(str[2:4])<32:
                if 0<int(str[0:2])<13:
                    return 1
            #ddmmyy
            elif 0<int(str[2:4])<13:
                if 0<int(str[0:2])<32:
                    return 1






    
result = where_is_year("260115")
print(result)
