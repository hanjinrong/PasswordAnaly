import glob
import os
import sys
import time
import re

def where_is_year(str):
    if len(str) == 8:
        #yyyymmdd
        if 1900 < int(str[0:4]) < 2016 and (0 < int(str[4:6]) < 13) and (0 < int(str[6:]) < 32):
            return True
            #ddmmyyyy
        elif 1900 < int(str[4:]) < 2016:
            if (0 < int(str[2:4]) < 13) and (0 < int(str[0:2]) < 32):
                return True
                #mmddyyyy
            elif(0 < int(str[2:4]) < 32) and (0 < int(str[0:2]) < 13):
                return True
    elif len(str) == 6:
        #yymmdd
        if 0 < int(str[0:2]) < 100 and 0 < int(str[2:4]) < 13 and 0 < int(str[4:]) < 32:
            return True
        #mmddyy
        elif 0 < int(str[4:]) < 100:
            if (0 < int(str[2:4]) < 32) and (0 < int(str[0:2]) < 13):
                return True
            #ddmmyy
            elif (0 < int(str[2:4]) < 13) and (0 < int(str[0:2]) < 32):
                return True
            

    #    for pinyin in pinyins:
    #        if(pinyin == 'an'):
    #            pass
    #        if(pinyin not in feature_statistic):
    #            feature_statistic[pinyin] = 1
    #        else:
    #            feature_statistic[pinyin] +=1
    #    #print(pinyin)
    #return feature_statistic

start = time.clock()

txt_filenames = glob.glob('F:\\Github\\KZ\\*.txt')
for filename in txt_filenames:
    match = re.match("(.*Pwd).txt", filename)
    if(not match):
        continue
    #if filename == "E:\\Github\\KZ\\163mailPwd.txt":
    txt_file = open(filename,'r',encoding='utf-8')
    f=open(match.group(1) + "Date.txt","w") 
    result = {}
    try:
        lines=txt_file.readlines()
        for line in lines:
            digit_strs = re.findall("\d+", line)
            for str in digit_strs:
                if(where_is_year(str)):
                    #print(str)
                    if(str not in result):
                        result[str] = 1
                    else:
                        result[str] += 1
        #f.writelines(result[0])

        for feature in result:
             f.writelines("%s\t\t%d\n" % (feature, result[feature]))
    finally:
        txt_file.close()
        f.close()

end=time.clock()
print ("read: %f s" % (end - start))