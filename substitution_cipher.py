#substitution cipher in python
#tugberk kocatekin
#march 2015

import math
from decimal import Decimal
from collections import Counter
text = "defendtheeastwallofthecastle"
key = "phqgiumeaylnofdxjkrcvstzwb"
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

def encrypt():
    alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
    new_map = {}



    # here we create a list where we can see new values for every char in alp
    for i in range(0, len(key)):
        new_map[alp[i]] = key[i]

    print new_map
      
    newtext = ""

    for i in range(0, len(text)):
        newtext = newtext + new_map[text[i]]

    print newtext

#encrypt()

#frequency analysis
'''
d  = collections.defaultdict(int)
for c in text:
    d[c] += 1
print d["t"]
'''

string = "KPUXBKIEKPYSSECPZDOHRRTIVZKXNOVRWMLSEIRRTBNMAKZWOWAGUIUQJDKHBVFXCMXAVWVJPZZLRVZRQMYXVKRXZLKZVHVRXMSEEOVVNIXICPRGZLTIKXKSZIILCMVGZWLIIMUIIKKEYPFADVMJBVFVBITMMEKMJVUJGLVIQQJIAGVWFMZGUMEKOPKWPIEIDAGPFSRJJZSSSHFGPUKRGEKMJVGXNGIMHMYGRRVXCQYEYPFANNUVASKINBUFRXROZVGWJICPVAZSTELKZLOWGEEGZAGRQSKLZZORSSIQVBOSAXYEOUGCASKFZMGWVPPHZBKGGIUJMWSSAPPEKPUXBKIEKPZLRMEZZAZMTEKSMACMYPUVVEUYGPFGVBOSAWFJZDOHRRTIVVJEYPFXCMXSONVGOAORGLVVJWSXUIJOZBILVWLWPIRPLHIERVLVBQRRVJUZRTFMIBUJIMVAIWZIFEIIOIQIAFPMIDKWGMXEOWXWGSVRNCXIZIDSMQFEGMFRJNZLRMIXCWAKUXJEILYYFTZGDWTWNFFYOLOJSIIIIBVMRGVWJNKZVHVRXMKZVHVRXMOWPSCPZKZIQXYVJCMLGAFAVGYJBVVRNQIWNRUMIBKVIMVANIRPSSIIIAOGRZZHZVIIVWSEBOKHFIGEMIZIYCKSKZKZRRKEIGIVBWJGJVZEZMEEOQURSSIIIAOGFYJINIBEEMVXTWLHVJWIMMTXGSFPNITHGITLIQWYRWWMIOKVCVZROKUPYITXDWTXUVFYBPZLRYJIJNMVRCFVWTGGXQRKIMZMPTFAYMXHAERRYWZLRVSSYQRCSPLMYAGVRGFPGMIXRHRRYENIGLVVDBOWUEZVJZLPHMUJJZLYEXYIMMDEZMEEOQURVRRPVJYLBIRRYBOVRTIMIBYGNRSIXWRPRGKIYCYMAKUIIBGPFXFRZMRIPXISIQIWNVVXVSKRSSIISISMAEKMJVHCNXVGCVOGNPVBKMXXGSJIVZILSSIJPZZLRVVZDLKRPIUSXCSIAXJJMWSXUIRVZIGVRECWJBGORRWSMNAVGLVVZFGQVRRXDWTEZQLRDBOSAEEHRMGTBRJEMMZEXIEJJZSEGGYMIOZSJSLRYAGRQFRPGQYXVGJTCWZSTVRTCAUJGSFPHIXOFEIIOIQIAFVGVCYIGLVCXITFRQRXXPKHGSRAZIVSAEKEGIZIEXZQZ"
string = string.lower()
#string = "giuifgceiiprctpnnduceiqprcni"
d = Counter(string.lower())

#print d.most_common(10)

vig_map = {}

for letter, freq in d.most_common(30):
    print '%s: %s' % (letter, freq)
    vig_map[letter] = freq

print vig_map
#####################
    
c = len(string) 
d = c * ( c - 1 ) / 26 

temp_ic = 0
ic = 0

c = len(string) 
d = c * ( c - 1 ) / 26

for i in range(1, 26):
    temp = vig_map[alp[i]]
    temp_ic = temp_ic + (temp * (temp - 1))

payda = len(string) * ( len(string) - 1 )


#print "ic: ", float(temp_ic) / float(payda)

##a function##
def ic(text):
    text = text.lower()
    c = len(text)
    d = c * ( c - 1 ) / 26
    temp_ic = 0
    ic = 0
    for i in range(1, 26):
        temp = vig_map[alp[i]]
        temp_ic = temp_ic + (temp * (temp - 1))

    payda = len(text) * ( len(text) - 1 )
    #print temp_ic
    #print payda
    print "ic: ", float(temp_ic) / float(payda)
    
    
#####create substrings######
sub_1 = ""
sub_2 = ""
sub_3 = ""
sub_4 = ""
sub_5 = ""
sub_6 = ""
sub_7 = ""
sub_8 = ""

k = 8
for i in range(0, int(math.floor(1200/k))):
    sub_1 += string[i*k + 1]
    sub_2 += string[i*k + 2]
    sub_3 += string[i*k + 3]
    sub_4 += string[i*k + 4]
    sub_5 += string[i*k + 5]
    sub_6 += string[i*k + 6]
    sub_7 += string[i*k + 7]
    sub_8 += string[i*k + 8]

print sub_1, sub_2

print ic(string)
   
print ic(sub_1), ic(sub_2), ic(sub_3), ic(sub_4), ic(sub_5), ic(sub_6), ic(sub_7), ic(sub_8)
