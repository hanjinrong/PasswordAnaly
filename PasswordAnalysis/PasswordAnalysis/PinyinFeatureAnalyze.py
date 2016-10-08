#match rime characters
import glob
import os
import sys
import time
import re
def match_a(buf):
    #a ai ao an ang
    if(buf[0:3] == 'ang'):
        return 'ang'
    elif(buf[0:2] == 'ai'):
        return 'ai'
    elif(buf[0:2] == 'ao'):
        return 'ao'
    elif(buf[0:2] == 'an'):
        return "an"
    elif(buf[0] == 'a'):
        return 'a'

def match_o(buf):
    #o ou ong
    if(buf[0:3] == 'ong'):
        return 'ong'
    elif(buf[0:2] == 'ou'):
        return 'ou'
    elif(buf[0] == 'o'):
        return 'o'

def match_e(buf):
    #e ei en eng
    if(buf[0:3] == 'eng'):
        return 'eng'
    elif(buf[0:2] == 'ei'):
        return 'ei'
    elif(buf[0:2] == 'en'):
        return 'en'
    elif(buf[0] == 'e'):
        return 'e'

def match_i(buf):
    #i ia ie iao iu ian in iang ing iong
    if(buf[0:4] == 'iong'):
        return 'iong'
    elif(buf[0:4] == 'iang'):
        return 'iang'
    elif(buf[0:3] == 'iao'):
        return 'iao'
    elif(buf[0:3] == 'ian'):
        return 'ian'
    elif(buf[0:3] == 'ing'):
        return 'ing'
    elif(buf[0:2] == 'ia'):
        return 'ia'
    elif(buf[0:2] == 'ie'):
        return 'ie'
    elif(buf[0:2] == 'iu'):
        return 'iu'
    elif(buf[0:2] == 'in'):
        return 'in'
    elif(buf[0] == 'i'):
        return 'i'

def match_u(buf):
    #u ua uo uai ui uan un uang ue
    if(buf[0:4] == 'uang'):
        return 'uang'
    elif(buf[0:3] == 'uai'):
        return 'uai'
    elif(buf[0:3] == 'uan'):
        return 'uan'
    elif(buf[0:2] == 'ua'):
        return 'ua'
    elif(buf[0:2] == 'uo'):
        return 'uo'
    elif(buf[0:2] == 'ui'):
        return 'ui'
    elif(buf[0:2] == 'un'):
        return 'un'
    elif(buf[0:2] == 'ue'):
        return 'ue'
    elif(buf[0] == 'u'):
        return 'u'

def match_v(buf):
    #v ve van vn 
    if(buf[0:3] == 'van'):
        return 'van'
    elif(buf[0:2] == 've'):
        return 've'
    elif(buf[0:2] == 'vn'):
        return 'vn'
    elif(buf[0] == 'v'):
        return 'v'

rime_table = {'a':match_a, 'o':match_o, 'e':match_e, 'i':match_i, 'u':match_u, 'v':match_v}

def match_rime(buf):
    return rime_table[buf[0]](buf)

#match onset characters
rule_out_b = ('be', 'bia', 'biang', 'biu', 'bong', 'bou', 'bua', 'buai', 'buan', 'buang', 
              'bue', 'bui', 'bun', 'buo', 'bv', 'bvan', 'bve', 'bvn')
def match_b(buf):
    result = 'b' + match_rime(buf[1:])
    if(result not in rule_out_b):
        return result

rule_out_p = ('pe', 'pia', 'piu', 'pong', 'pua', 'puan', 'pue', 'pui', 'pun', 'puo'
              'pv', 'pvan', 'pve', 'pvn')
def match_p(buf):
    result = 'p' + match_rime(buf[1:])
    if(result not in rule_out_p):
        return result 

rule_out_m = ('mia', 'miang', 'mong', 'mua', 'muan', 'muang', 'mue', 'mui', 'mun', 'muo'
              'mv', 'mvan', 'mve', 'mvn')
def match_m(buf):
    result = 'm' + match_rime(buf[1:])
    if(result not in rule_out_m):
        return result 

rule_out_f = ('fai', 'fao', 'fe', 'fi', 'fia', 'fian', 'fie', 'fin', 'fing', 'fiong',
              'fiu', 'fong', 'fua', 'fue', 'fui', 'fun', 'fuo', 'fv', 'fve', 'fvn')
def match_f(buf):
    result = 'f' + match_rime(buf[1:])
    if(result not in rule_out_f):
        return result 

rule_out_d = ('diang', 'din', 'diong', 'do', 'dua', 'duang', 'due', 'dv', 'dvan', 'dve', 'dvn')
def match_d(buf):
    result = 'd' + match_rime(buf[1:])
    if(result not in rule_out_d):
        return result 

rule_out_t = ('ten', 'tia', 'tiang', 'tin', 'tiu', 'to', 'tua', 'tuai', 'tue', 'tv'
              'tvan', 'tve', 'tvn', 'wao', 'we')
def match_t(buf):
    result = 't' + match_rime(buf[1:])
    if(result not in rule_out_t):
        return result 

rule_out_n = ('nia', 'no', 'nua', 'nuai', 'nui', 'nun', 'nvan', 'nvn')
def match_n(buf):
    result = 'n' + match_rime(buf[1:])
    if(result not in rule_out_n):
        return result 

rule_out_l = ('len', 'lua', 'luai', 'luang', 'lui', 'lvan', 'lvn')
def match_l(buf):
    result = 'l' + match_rime(buf[1:])
    if(result not in rule_out_l):
        return result 

rule_out_g = ('gi', 'gia', 'gian', 'giang', 'giao', 'gie', 'gin', 'ging', 'giu', 'go'
              'gue', 'gv', 'gvan', 'gve', 'gvn')
def match_g(buf):
    result = 'g' + match_rime(buf[1:])
    if(result not in rule_out_g):
        return result 

rule_out_k = ('kei', 'ki', 'kia', 'kian', 'kiang', 'kiao', 'kie', 'kin', 'king', 'kiong',
              'kiu', 'ko', 'kue', 'kv', 'kvan', 'kve', 'kvn')
def match_k(buf):
    result = 'k' + match_rime(buf[1:])
    if(result not in rule_out_k):
        return result 

rule_out_h = ('hi', 'hia', 'hian', 'hiang', 'hie', 'hin', 'hing', 'hiu', 'ho', 'hue',
              'hv', 'hvan', 'hve', 'hvn')
def match_h(buf):
    result = 'h' + match_rime(buf[1:])
    if(result not in rule_out_h):
        return result 
    
rule_out_j = ('ja', 'jai', 'jan', 'jang', 'jao', 'je', 'jei', 'jen', 'jeng', 'jin'
              'jo', 'jong', 'jou', 'jua', 'juai', 'juang', 'jui', 'juo')
def match_j(buf):
    result = 'j' + match_rime(buf[1:])
    if(result not in rule_out_j):
        return result 

rule_out_q = ('qa', 'qai', 'qan', 'qao', 'qe', 'qei', 'qeng', 'qo', 'qua', 'quai'
              'quang', 'qui', 'quo')
def match_q(buf):
    result = 'q' + match_rime(buf[1:])
    if(result not in rule_out_q):
        return result 

rule_out_x = ('xai', 'xan', 'xang', 'xao', 'xe', 'xei', 'xen', 'xin', 'xing', 'xo'
              'xong', 'xou', 'xua', 'xui', 'xuo')
def match_x(buf):
    result = 'x' + match_rime(buf[1:])
    if(result not in rule_out_x):
        return result 

rule_out_z = ('zia', 'zian', 'zie', 'zin', 'zing', 'ziu', 'zo', 'zua', 'zue', 'zv'
              'zvan', 'zve', 'zvn')
rule_out_zh = ('zhei', 'zhian', 'zhie', 'zhin', 'zho')
def match_z(buf):
    #z, zh
    if(buf[0:2] == 'zh'):
        result = 'zh' + match_rime(buf[2:])
        if(result not in rule_out_zh):
            return result 
    else:
        result = 'z' + match_rime(buf[1:])
        if(result not in rule_out_z):
            return result

rule_out_c = ('cei', 'cia', 'cian', 'ciang', 'ciao', 'cie', 'cin', 'cing', 'ciu', 'co'
              'cua', 'cue', 'cv', 'cvan', 'cve', 'cvn')
rule_out_ch = ('chei', 'chia', 'chian', 'chiang', 'chiao', 'chie', 'chin', 'ching', 'chiu'
               'cho', 'chue', 'chv', 'chvan', 'chve')
def match_c(buf):
    #c, ch
    result = ''
    if(buf[0:2] == 'ch'):
        result = 'ch' + match_rime(buf[2:])
        if(result not in rule_out_ch):
            return result 
    else:
        result = 'c' + match_rime(buf[1:])
        if(result not in rule_out_c):
            return result 

rule_out_s = ('sei', 'sia', 'sian', 'siang', 'siao', 'sie', 'sin', 'sing', 'siu', 'so',
              'sou', 'sua', 'suai', 'suan', 'sue', 'sv', 'svan', 'sve', 'svn')
rule_out_sh = ('shia', 'shian', 'shiao', 'shie', 'shin', 'shing', 'shiong', 'shiu', 'sho', 'shong',
               'shue', 'shv', 'shvan', 'shve')
def match_s(buf):
    #s, sh
    result = ''
    if(buf[0:2] == 'sh'):
        result = 'sh' + match_rime(buf[2:])
        if(result not in rule_out_sh):
            return result 
    else:
        result = 's' + match_rime(buf[1:])
        if(result not in rule_out_s):
            return result 

rule_out_r = ('ra', 'rai', 'rei', 'ria', 'rian', 'riang', 'riao', 'rie', 'rin', 'ring',
              'riong', 'riu', 'ro', 'rua', 'ruai', 'ruang', 'rue', 'rv', 'rvan', 'rve',
              'rvn',)
def match_r(buf):
    result = 'r' + match_rime(buf[1:])
    if(result not in rule_out_r):
        return result 

rule_out_y = ('yai', 'yei', 'yen', 'yeng', 'yia', 'yian', 'yie', 'yiu', 'yo', 'yua'
              'yui', 'yuo', 'yv', 'yvan', 'yve', 'yvn')
def match_y(buf):
    result = 'y' + match_rime(buf[1:])
    if(result not in rule_out_y):
        return result 

rule_out_w = ('wi', 'wia', 'wian', 'wie', 'win', 'wing', 'wiu', 'wong', 'wou', 'wua'
              'wuan', 'wue', 'wui', 'wun', 'wuo', 'wv', 'wvan', 'wve', 'wvn', 'xa')
def match_w(buf):
    result = 'w' + match_rime(buf[1:])
    if(result not in rule_out_w):
        return result 

onset_table = {'b':match_b, 'p':match_p, 'm':match_m, 'f':match_f, 
               'd':match_d, 't':match_t, 'n':match_n, 'l':match_l,
               'g':match_g, 'k':match_k, 'h':match_h, 'j':match_j, 'q':match_q, 'x':match_x, 
               'z':match_z, 'c':match_c, 's':match_s, 'r':match_r, 'y':match_y, 'w':match_w}

single_rime_word_table = ('ang', 'ai', 'ao', 'an', 'a', 'ou', 'o', 'eng', 'ei', 'en', 'e')
def match_single_rime_word(buf):
    if(buf[0:3] in single_rime_word_table):
        return buf[0:3]
    elif(buf[0:2] in single_rime_word_table):
        return buf[0:2]
    elif(buf[0] in single_rime_word_table):
        return buf[0]

def match_onset(buf):
    try:
        if(buf[0] in onset_table):
            return onset_table[buf[0]](buf)
        else:
            return match_single_rime_word(buf)
    except:
        return None



def readLines(lines):
    feature_statistic = {}
    for line in lines:
        line = line.lower()
        while(len(line) > 0):
            pinyin = ""
            pinyin = match_onset(line)
            if(pinyin):
                if(pinyin not in feature_statistic):
                    feature_statistic[pinyin] = 1
                else:
                    feature_statistic[pinyin] +=1
                line = line[len(pinyin):]
                #print(pinyin)
            else:
                line = line[1:]
    return feature_statistic

start = time.clock()

txt_filenames = glob.glob('E:\\Github\\KZ\\*.txt')
for filename in txt_filenames:
    match = re.match("(.*Pwd).txt", filename)
    if(not match):
        continue
    #if filename == "E:\\Github\\KZ\\163mailPwd.txt":
    txt_file = open(filename,'r',encoding='utf-8')
    f=open(match.group(1) + "PinYin.txt","w") 
    try:
        lines=txt_file.readlines()
        result = readLines(lines)
        #f.writelines(result[0])

        for feature in result:
             f.writelines("%s\t\t%d\n" % (feature, result[feature]))
    finally:
        txt_file.close()
        f.close()

end=time.clock()
print ("read: %f s" % (end - start))