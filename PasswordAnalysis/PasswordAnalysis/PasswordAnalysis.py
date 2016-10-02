#encoding='UTF-8'

import glob
import os
import sys

txt_filenames = glob.glob('E:\Github\KZ\*.txt')
for filename in txt_filenames:
    if filename =="E:\\Github\\KZ\\163mail.txt":
        txt_file = open(filename,'r',encoding='utf-8')
        f=open("E:\\Github\\KZ\\163mailPwd.txt","w")
        pwdList=[]
        try:
            lines=txt_file.readlines();
            for line in lines:
                splitLine=line.split('----')
                pwdList.append(splitLine[1])
            f.writelines(pwdList)
        finally:
            txt_file.close()
    elif filename =="E:\\Github\\KZ\\linkedin.csv.txt":
        txt_file = open(filename,'r',encoding='utf-8')
        f=open("E:\\Github\\KZ\\linkedinPwd.txt","w")
        pwdList=[]
        try:
            lines=txt_file.readlines();
            for line in lines:
                splitLine=line.split(':')
                pwdList.append(splitLine[1])
            f.writelines(pwdList)
        finally:
            txt_file.close()
    elif filename =="E:\\Github\\KZ\\plaintxt_yahoo1.txt":
        txt_file = open(filename,'r',encoding='utf-8')
        f=open("E:\\Github\\KZ\\yahooPwd.txt","w")
        pwdList=[]
        try:
            lines = txt_file.readlines();
            for line in lines:
                splitLine = line.split(':')
               # print(splitLine)
                try:
                    pwdList.append(splitLine[2])
                except:
                    pass
            f.writelines(pwdList)
        finally:
            txt_file.close()
    else:
        pass

#file_object = open("E:\Github\conciseoxforddic00fowlrich.txt","r",encoding='UTF-8')
#try:
#     all_the_text = file_object.read( )
#     print(all_the_text);
#finally:
#     file_object.close( )
#import os
#from os.path import join
 
#def main() :
#    dest = "d:/project/"
#    outfile = open( "output.txt", "w" )
#    for root, dirs, files in os.walk( dest ):
#        for OneFileName in files :
#            if OneFileName.find( '.txt' ) == -1 :
#                continue
#            OneFullFileName = join( root, OneFileName )
#            for line in open( OneFullFileName ):
#                print( line, end = '' )
# 
#if __name__ == "__main__" :
#    main()
   # elif filename =="E:\\Github\\KZ\\linkedin.csv.txt":
   #     txt_file = open(filename,'r',encoding='utf-8')
   #     try:
   #         lines=txt_file.readlines():