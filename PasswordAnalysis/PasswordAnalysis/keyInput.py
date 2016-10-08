#import glob
#import os
#import sys
#import time
#start = time.clock()
#dict1={'~':(0,-1),'`':(0,-1),'!':(0,0),'@':(0,1),'#':(0,2),'1':(0,0),'2':(0,1),'3':(0,2),'4':(0,3),'$':(0,3),'5':(0,4),'%':(0,4),'6':(0,5),'^':(0,5),'7':(0,6),'&':(0,6),'8':(0,7),'*':(0,7),'9':(0,8),'(':(0,8),'0':(0,9),')':(0,9),'_':(0,10),'-':(0,10),'+':(0,11),'=':(0,11),
#    'q':(1,0),'w':(1,1),'e':(1,2),'r':(1,3),'t':(1,4),'y':(1,5),'u':(1,6),'i':(1,7),'o':(1,8),'p':(1,9),'[':(1,10),'{':(1,10),']':(1,11),'}':(1,11),'|':(1,12),'\\':(1,12),
#    'a':(2,0),'s':(2,1),'d':(2,2),'f':(2,3),'g':(2,4),'h':(2,5),'j':(2,6),'k':(2,7),'l':(2,8),';':(2,9),':':(2,9),'\'':(2,10),'"':(2,10),
#    'z':(3,0),'x':(3,1),'c':(3,2),'v':(3,3),'b':(3,4),'n':(3,5),'m':(3,6),',':(3,7),'<':(3,7),'.':(3,8),'>':(3,8),'/':(3,9),'?':(3,9),
#    }
#txt_filenames = glob.glob('E:\Github\KZ\*.txt')
#for filename in txt_filenames:
#    if filename =="E:\\Github\\KZ\\163mailPwd.txt":
#        txt_file = open(filename,'r',encoding='utf-8')
#        f=open("E:\\Github\\KZ\\163mailPwdKeyPattern.txt","w")
#        pwdKey=[]
#        try:
#            lines=txt_file.readlines();
#            for line in lines:
#                line = line.lower()
#                for index in range(len(line)-3):
#                    index=index+1
#                    if ((abs(dict1[line[index+1]][0]-dict1[line[index-1]][0])==2)&(abs(dict1[line[index+1]][1]-dict1[line[index-1]][1])==0)&(abs(dict1[line[index]][0]-dict1[line[index+1]][0])==1)&(abs(dict1[line[index]][1]-dict1[line[index+1]][1])==0)&(abs(dict1[line[index]][0]-dict1[line[index-1]][0])==1)&(abs(dict1[line[index]][1]-dict1[line[index-1]][1])==0))|((abs(dict1[line[index+1]][1]-dict1[line[index-1]][1])==2)&(abs(dict1[line[index+1]][0]-dict1[line[index-1]][0])==0)&(abs(dict1[line[index]][0]-dict1[line[index+1]][0])==0)&(abs(dict1[line[index]][1]-dict1[line[index+1]][1])==1)&(abs(dict1[line[index]][0]-dict1[line[index-1]][0])==0)&(abs(dict1[line[index]][1]-dict1[line[index-1]][1])==1)):
#                        print(line)
#                        pwdKey.append(line)
#                        break
#            f.writelines(pwdKey)
#        finally:
#            txt_file.close()
#end=time.clock()
#print ("read: %f s" % (end - start))
import glob
import os
import sys
import time
import re

def handle_file(lines):
    #pwdKey = []
    feature_statistic = {}

    for line in lines:
        line = line.lower()
        for index in range(1, len(line) - 2, 1):
            if (((abs(dict1[line[index + 1]][0] - dict1[line[index - 1]][0]) == 2) and
                (abs(dict1[line[index + 1]][1] - dict1[line[index - 1]][1]) == 0) and
                (abs(dict1[line[index]][0] - dict1[line[index + 1]][0]) == 1) and 
                (abs(dict1[line[index]][1] - dict1[line[index + 1]][1]) == 0) and
                (abs(dict1[line[index]][0] - dict1[line[index-1]][0]) == 1) and
                (abs(dict1[line[index]][1] - dict1[line[index-1]][1]) == 0)) or
               ((abs(dict1[line[index + 1]][1] - dict1[line[index - 1]][1]) == 2) and
                (abs(dict1[line[index + 1]][0] - dict1[line[index - 1]][0]) == 0) and
                (abs(dict1[line[index]][0] - dict1[line[index + 1]][0]) == 0) and
                (abs(dict1[line[index]][1] - dict1[line[index + 1]][1]) == 1) and
                (abs(dict1[line[index]][0] - dict1[line[index - 1]][0]) == 0) and
                (abs(dict1[line[index]][1] - dict1[line[index - 1]][1]) == 1))):
                #print(line)
                #pwdKey.append(line)
                feature = line[index - 1: index + 2]
                if(feature not in feature_statistic):
                    feature_statistic[feature] = 1
                else:
                    feature_statistic[feature] += 1
                break

    return feature_statistic

dict1={'~':(0,-1),'`':(0,-1),'!':(0,0),'@':(0,1),'#':(0,2),'1':(0,0),'2':(0,1),'3':(0,2),'4':(0,3),'$':(0,3),'5':(0,4),'%':(0,4),'6':(0,5),'^':(0,5),'7':(0,6),'&':(0,6),'8':(0,7),'*':(0,7),'9':(0,8),'(':(0,8),'0':(0,9),')':(0,9),'_':(0,10),'-':(0,10),'+':(0,11),'=':(0,11),
    'q':(1,0),'w':(1,1),'e':(1,2),'r':(1,3),'t':(1,4),'y':(1,5),'u':(1,6),'i':(1,7),'o':(1,8),'p':(1,9),'[':(1,10),'{':(1,10),']':(1,11),'}':(1,11),'|':(1,12),'\\':(1,12),
    'a':(2,0),'s':(2,1),'d':(2,2),'f':(2,3),'g':(2,4),'h':(2,5),'j':(2,6),'k':(2,7),'l':(2,8),';':(2,9),':':(2,9),'\'':(2,10),'"':(2,10),
    'z':(3,0),'x':(3,1),'c':(3,2),'v':(3,3),'b':(3,4),'n':(3,5),'m':(3,6),',':(3,7),'<':(3,7),'.':(3,8),'>':(3,8),'/':(3,9),'?':(3,9),' ':(-255,-255),
    }

start = time.clock()

txt_filenames = glob.glob('E:\\Github\\KZ\\*.txt')
for filename in txt_filenames:
    match = re.match("(.*Pwd).txt", filename)
    if(not match):
        continue
    #if filename == "E:\\Github\\KZ\\163mailPwd.txt":
    txt_file = open(filename,'r',encoding='utf-8')
    f=open(match.group(1) + "Pattern.txt","w") 
    try:
        lines=txt_file.readlines()
        result = handle_file(lines)
        #f.writelines(result[0])

        for feature in result:
             f.writelines("%s\t\t%d\n" % (feature, result[feature]))
    finally:
        txt_file.close()
        f.close()

end=time.clock()
print ("read: %f s" % (end - start))

#def is_adjacency(a, b, c):
#    if(abs(dict(a)[0] - dict(b)[0]) == 1) and
#        (abs(dict(a)[1] - ))
