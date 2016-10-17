#match rime characters
import glob
import os
import sys
import time
import re

def match_a(buf):
    #a ai ao an ang
    result = []

    if(buf[0:3] == 'ang'):
        result.append('ang')
    if(buf[0:2] == 'ai'):
        result.append('ai')
    if(buf[0:2] == 'ao'):
        result.append('ao')
    if(buf[0:2] == 'an'):
        result.append('an')
    if(buf[0] == 'a'):
        result.append('a')
    return result

def match_o(buf):
    #o ou ong
    result = []

    if(buf[0:3] == 'ong'):
        result.append('ong')
    if(buf[0:2] == 'ou'):
        result.append('ou')
    if(buf[0] == 'o'):
        result.append('o')
    return result

def match_e(buf):
    #e ei en eng
    result = []

    if(buf[0:3] == 'eng'):
        result.append('eng')
    if(buf[0:2] == 'ei'):
        result.append('ei')
    if(buf[0:2] == 'en'):
        result.append('en')
    if(buf[0] == 'e'):
        result.append('e')
    return result

def match_i(buf):
    #i ia ie iao iu ian in iang ing iong
    result = []

    if(buf[0:4] == 'iong'):
        result.append('iong')
    if(buf[0:4] == 'iang'):
        result.append('iang')
    if(buf[0:3] == 'iao'):
        result.append('iao')
    if(buf[0:3] == 'ian'):
        result.append('ian')
    if(buf[0:3] == 'ing'):
        result.append('ing')
    if(buf[0:2] == 'ia'):
        result.append('ia')
    if(buf[0:2] == 'ie'):
        result.append('ie')
    if(buf[0:2] == 'iu'):
        result.append('iu')
    if(buf[0:2] == 'in'):
        result.append('in')
    if(buf[0] == 'i'):
        result.append('i')
    return result

def match_u(buf):
    #u ua uo uai ui uan un uang ue
    result = []

    if(buf[0:4] == 'uang'):
        result.append('uang')
    if(buf[0:3] == 'uai'):
        result.append('uai')
    if(buf[0:3] == 'uan'):
        result.append('uan')
    if(buf[0:2] == 'ua'):
        result.append('ua')
    if(buf[0:2] == 'uo'):
        result.append('uo')
    if(buf[0:2] == 'ui'):
        result.append('ui')
    if(buf[0:2] == 'un'):
        result.append('un')
    if(buf[0:2] == 'ue'):
        result.append('ue')
    if(buf[0] == 'u'):
        result.append('u')
    return result

def match_v(buf):
    #v ve van vn 
    result = []

    if(buf[0:3] == 'van'):
        result.append('van')
    if(buf[0:2] == 've'):
        result.append('ve')
    if(buf[0:2] == 'vn'):
        result.append('vn')
    if(buf[0] == 'v'):
        result.append('v')
    return result

rime_table = {'a':match_a, 'o':match_o, 'e':match_e, 'i':match_i, 'u':match_u, 'v':match_v}

def match_rime(buf):
    return rime_table[buf[0]](buf)

#match onset characters
rule_out_b = ('be', 'bia', 'biang', 'biu', 'bong', 'bou', 'bua', 'buai', 'buan', 'buang', 
              'bue', 'bui', 'bun', 'buo', 'bv', 'bvan', 'bve', 'bvn')
def match_b(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'b' + rime
        if(result not in rule_out_b):
            return result

rule_out_p = ('pe', 'pia', 'piu', 'pong', 'pua', 'puan', 'puang', 'pue', 'pui', 'pun', 'puo',
              'pv', 'pvan', 'pve', 'pvn')
def match_p(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'p' + rime
        if(result not in rule_out_p):
            return result

rule_out_m = ('mia', 'miang', 'mong', 'mua', 'muan', 'muang', 'mue', 'mui', 'mun', 'muo',
              'mv', 'mvan', 'mve', 'mvn')
def match_m(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'm' + rime
        if(result not in rule_out_m):
            return result

rule_out_f = ('fai', 'fao', 'fe', 'fi', 'fia', 'fian', 'fie', 'fin', 'fing', 'fiong',
              'fiu', 'fong', 'fua', 'fuai', 'fue', 'fui', 'fun', 'fuo', 'fv', 'fve', 'fvn')
def match_f(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'f' + rime
        if(result not in rule_out_f):
            return result

rule_out_d = ('diang', 'din', 'diong', 'do', 'dua', 'duai', 'duang', 'due', 'dv', 'dvan', 'dve', 'dvn')
def match_d(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'd' + rime
        if(result not in rule_out_d):
            return result

rule_out_t = ('ten', 'tia', 'tiang', 'tin', 'tiu', 'tiong', 'to', 'tua', 'tuai', 
              'tuang', 'tue', 'tv', 'tvan', 'tve', 'tvn', 'wao', 'we')
def match_t(buf):
    if(buf[1] == 'v'):
        return None
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 't' + rime
        if(result not in rule_out_t):
            return result

rule_out_n = ('nia', 'niong', 'no', 'nua', 'nuang', 'nuai', 'nui', 'nue', 'nun', 'nvan', 'nvang', 'nvn')
def match_n(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'n' + rime
        if(result not in rule_out_n):
            return result

rule_out_l = ('len', 'lua', 'luai', 'lue', 'luang', 'lui', 'lvan', 'lvn', 'lo')
def match_l(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'l' + rime
        if(result not in rule_out_l):
            return result

rule_out_g = ('gi', 'gia', 'gian', 'giang', 'giao', 'gie', 'gin', 'ging', 'giu', 'go',
              'gue', 'gv', 'gvan', 'gve', 'gvn')
def match_g(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'g' + rime
        if(result not in rule_out_g):
            return result

rule_out_k = ('kei', 'ki', 'kia', 'kian', 'kiang', 'kiao', 'kie', 'kin', 'king', 'kiong',
              'kiu', 'ko', 'kue', 'kv', 'kvan', 'kve', 'kvn')
def match_k(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'k' + rime
        if(result not in rule_out_k):
            return result

rule_out_h = ('hi', 'hia', 'hian', 'hiang', 'hie', 'hin', 'hing', 'hiu', 'ho', 'hue',
              'hv', 'hvan', 'hve', 'hvn')
def match_h(buf):
    if(buf[1] == 'i'):
        return None
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'h' + rime
        if(result not in rule_out_h):
            return result
    
rule_out_j = ('ja', 'jai', 'jan', 'jang', 'jao', 'je', 'jei', 'jen', 'jeng', 'jin',
              'jo', 'jong', 'jou', 'jua', 'juai', 'juang', 'jui', 'juo')
def match_j(buf):
    if(buf[1] == 'v'):
        return None
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'j' + rime
        if(result not in rule_out_j):
            return result

rule_out_q = ('qa', 'qai', 'qan', 'qao', 'qe', 'qen', 'qei', 'qeng', 'qo', 'qou', 'qua', 'quai',
              'quang', 'qui', 'quo')
def match_q(buf):
    if(buf[1] == 'v'):
        return None
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'q' + rime
        if(result not in rule_out_q):
            return result

rule_out_x = ('xa', 'xai', 'xan', 'xang', 'xao', 'xe', 'xei', 'xen', 'xeng', 'xin', 'xing', 'xo',
              'xong', 'xou', 'xua', 'xui', 'xuo')
def match_x(buf):
    if(buf[1] == 'v'):
        return None
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'x' + rime
        if(result not in rule_out_x):
            return result

rule_out_z = ('zia', 'ziao','zian', 'zie', 'zin', 'zing', 'ziong', 'ziu', 'zo', 'zua', 'zue', 'zv',
              'zvan', 'zve', 'zvn', 'zuai')
rule_out_zh = ('zhei', 'zhian', 'zhiao', 'zhie', 'zhin', 'zhiong', 'zho')
def match_z(buf):
    #z, zh
    if(buf[0:2] == 'zh'):
        possible_rime = match_rime(buf[1:])
        for rime in possible_rime:
            result = 'zh' + rime
            if(result not in rule_out_zh):
                return result
    else:
        possible_rime = match_rime(buf[1:])
        for rime in possible_rime:
            result = 'z' + rime
            if(result not in rule_out_z):
                return result

rule_out_c = ('cei', 'cia', 'cian', 'ciang', 'ciao', 'cie', 'cin', 'cing', 'ciu', 'co',
              'cua', 'cue', 'cv', 'cvan', 'cve', 'cvn')
rule_out_ch = ('chei', 'chia', 'chian', 'chiang', 'chiao', 'chie', 'chin', 'ching', 'chiu',
               'cho', 'chue', 'chv', 'chvan', 'chve')
def match_c(buf):
    #c, ch
    result = ''
    if(buf[0:2] == 'ch'):
        possible_rime = match_rime(buf[1:])
        for rime in possible_rime:
            result = 'ch' + rime
            if(result not in rule_out_ch):
                return result
    else:
        possible_rime = match_rime(buf[1:])
        for rime in possible_rime:
            result = 'c' + rime
            if(result not in rule_out_c):
                return result

rule_out_s = ('sei', 'sia', 'sian', 'siang', 'siao', 'sie', 'sin', 'sing', 'siu', 'siong', 'so',
              'sou', 'sua', 'suai', 'suan', 'sue', 'sv', 'svan', 'sve', 'svn')
rule_out_sh = ('shia', 'shian', 'shiao', 'shie', 'shin', 'shing', 'shiong', 'shiu', 'sho', 'shong',
               'shue', 'shv', 'shvan', 'shve')
def match_s(buf):
    #s, sh
    result = ''
    if(buf[0:2] == 'sh'):
        possible_rime = match_rime(buf[1:])
        for rime in possible_rime:
            result = 'sh' + rime
            if(result not in rule_out_sh):
                return result
    else:
        possible_rime = match_rime(buf[1:])
        for rime in possible_rime:
            result = 's' + rime
            if(result not in rule_out_s):
                return result

rule_out_r = ('ra', 'rai', 'rei', 'ria', 'rian', 'riang', 'riao', 'rie', 'rin', 'ring',
              'riong', 'riu', 'ro', 'rua', 'ruai', 'ruang', 'rue', 'rv', 'rvan', 'rve',
              'rvn',)
def match_r(buf):
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'r' + rime
        if(result not in rule_out_r):
            return result

rule_out_y = ('yai', 'yei', 'yen', 'yeng', 'yia', 'yian', 'yiang', 'yie', 'yiu', 'yo', 'yua', 'yuai'
              'yui', 'yuo')
def match_y(buf):
    if(buf[1] == 'i' or buf[1] == 'v'):
        return None
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'y' + rime
        if(result not in rule_out_y):
            return result

rule_out_w = ('wi', 'wia', 'wian', 'wie', 'win', 'wing', 'wiu', 'wong', 'wou', 'wv', 
              'wvan', 'wve', 'wvn', 'we')
def match_w(buf):
    if(buf[1] == 'u' or buf[1] == 'i' or buf[1] == 'v'):
        return None
    possible_rime = match_rime(buf[1:])
    for rime in possible_rime:
        result = 'w' + rime
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
        words = re.findall('[a-z]+', line)
        pinyins = []
        for word in words:
            tmp = word
            while(len(tmp) > 0):
                pinyin = ""
                pinyin = match_onset(tmp)
                if(pinyin):
                    pinyins.append(pinyin)
                    tmp = tmp[len(pinyin):]
                else:
                    pinyins.clear()
                    break
            if(len(pinyins) == 0):
                break

        for pinyin in pinyins:
            if(pinyin == 'an'):
                pass
            if(pinyin not in feature_statistic):
                feature_statistic[pinyin] = 1
            else:
                feature_statistic[pinyin] +=1
        #print(pinyin)
    return feature_statistic

line = "hanhanhanchozuaigo"
while(len(line) > 0):
    pinyin = ""
    pinyin = match_onset(line)
    if(pinyin):
        line = line[len(pinyin):]
        print(pinyin)
    else:
        line = line[1:]
print("end of test")

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