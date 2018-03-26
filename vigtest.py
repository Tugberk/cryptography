#!/usr/bin/python
#vigenere cryptanalysis

import math
from decimal import Decimal
from collections import Counter

alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#print alp.index('z')
eng_alp = {"e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7, "n": 6.7, "s": 6.3, "h": 6.1, "r": 6, "d": 4.3, "l": 4, "u": 2.8, "c":2.8, "m": 2.4, "w": 2.4, "f": 2.2, "y": 2, "g": 2, "p": 1.9, "b": 1.5, "v": 1, "k": 0.8, "x": 0.2, "j":0.2, "q": 0.1, "z":0.1}




def ic(text):
	vig_map = {}
	text = text.lower()
	d = Counter(text)

	for letter, freq in d.most_common(30):
		vig_map[letter] = freq

	#print vig_map
	textlength = len(text)
#	d = textlength * (textlength - 1)
	temp_ic = 0
	for i in range(0, 26):
		if alp[i] in vig_map:
			temp = vig_map[alp[i]]
		else:
			temp = 0
		#temp = vig_map[alp[i]]
		temp_ic += temp * (temp - 1)
	payda = textlength * (textlength - 1)
	print "ic: ", float(temp_ic) / float(payda)




# creating substrings
sub_1 = ""
sub_2 = ""
sub_3 = ""
sub_4 = ""
sub_5 = ""
sub_6 = ""
sub_7 = ""
sub_8 = ""




#string = "vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt"
string = "KPUaXBKIEKPYSSECPZDOHRRTIVZKXNOVRWMLSEIRRTBNMAKZWOWAGUIUQJDKHBVFXCMXAVWVJPZZLRVZRQMYXVKRXZLKZVHVRXMSEEOVVNIXICPRGZLTIKXKSZIILCMVGZWLIIMUIIKKEYPFADVMJBVFVBITMMEKMJVUJGLVIQQJIAGVWFMZGUMEKOPKWPIEIDAGPFSRJJZSSSHFGPUKRGEKMJVGXNGIMHMYGRRVXCQYEYPFANNUVASKINBUFRXROZVGWJICPVAZSTELKZLOWGEEGZAGRQSKLZZORSSIQVBOSAXYEOUGCASKFZMGWVPPHZBKGGIUJMWSSAPPEKPUXBKIEKPZLRMEZZAZMTEKSMACMYPUVVEUYGPFGVBOSAWFJZDOHRRTIVVJEYPFXCMXSONVGOAORGLVVJWSXUIJOZBILVWLWPIRPLHIERVLVBQRRVJUZRTFMIBUJIMVAIWZIFEIIOIQIAFPMIDKWGMXEOWXWGSVRNCXIZIDSMQFEGMFRJNZLRMIXCWAKUXJEILYYFTZGDWTWNFFYOLOJSIIIIBVMRGVWJNKZVHVRXMKZVHVRXMOWPSCPZKZIQXYVJCMLGAFAVGYJBVVRNQIWNRUMIBKVIMVANIRPSSIIIAOGRZZHZVIIVWSEBOKHFIGEMIZIYCKSKZKZRRKEIGIVBWJGJVZEZMEEOQURSSIIIAOGFYJINIBEEMVXTWLHVJWIMMTXGSFPNITHGITLIQWYRWWMIOKVCVZROKUPYITXDWTXUVFYBPZLRYJIJNMVRCFVWTGGXQRKIMZMPTFAYMXHAERRYWZLRVSSYQRCSPLMYAGVRGFPGMIXRHRRYENIGLVVDBOWUEZVJZLPHMUJJZLYEXYIMMDEZMEEOQURVRRPVJYLBIRRYBOVRTIMIBYGNRSIXWRPRGKIYCYMAKUIIBGPFXFRZMRIPXISIQIWNVVXVSKRSSIISISMAEKMJVHCNXVGCVOGNPVBKMXXGSJIVZILSSIJPZZLRVVZDLKRPIUSXCSIAXJJMWSXUIRVZIGVRECWJBGORRWSMNAVGLVVZFGQVRRXDWTEZQLRDBOSAEEHRMGTBRJEMMZEXIEJJZSEGGYMIOZSJSLRYAGRQFRPGQYXVGJTCWZSTVRTCAUJGSFPHIXOFEIIOIQIAFVGVCYIGLVCXITFRQRXXPKHGSRAZIVSAEKEGIZIEXZQZ"
string = string.lower()

#print vig_map_string


def chi_square_fn(text):

    # frequency analysis
    vig_map_string = {}
    cnt = Counter(text)
    for letter, freq in cnt.most_common(100):
        vig_map_string[letter] = freq


    expected = []

    for i in range(0, len(alp)):
        #print "text length ", len(text)
        #print "exp value ", eng_alp[alp[i]]
        deger = float(len(text)) * float(eng_alp[alp[i]]) / float(100)
        #print deger
        #print "deneme", eng_alp[alp[i]]
        expected.append(deger)
    
    #print expected

    chi_square = []
    for i in range(0, len(alp)):
            if not alp[i] in vig_map_string:
                #calc = (len(text) - int(vig_map_string[alp[i+1]])) ** 2 / expected[i+1]
                calc = 0
            else:
                calc = (int(vig_map_string[alp[i]]) - expected[i]) ** 2 / expected[i]
            chi_square.append(calc)

    #print "total chi square is", sum(chi_square)
    return int(sum(chi_square))



k = 8


for i in range(0, int(math.floor(len(string) / k))):
    sub_1 += string[i*k]
    sub_2 += string[i*k + 2 - 1]
    sub_3 += string[i*k + 3 - 1]
    sub_4 += string[i*k + 4 - 1]
    sub_5 += string[i*k + 5 - 1]
    sub_6 += string[i*k + 6 - 1]
    sub_7 += string[i*k + 7 - 1]
    sub_8 += string[i*k + 8 - 1]

sub = []
sub.append(sub_1)
sub.append(sub_2)
sub.append(sub_3)
sub.append(sub_4)
sub.append(sub_5)
sub.append(sub_6)
sub.append(sub_7)
sub.append(sub_8)



keyword = []

def analiz(text):

    newlist = []
    for j in range(0, 26):
        sub_shift = ""
        for char in text:
            i_new = alp.index(char) - j
            if i_new < 0: #for negative numbers
                i_new = i_new + 26
            #print i_new
            sub_shift += alp[i_new]
        print sub_shift
        value = chi_square_fn(sub_shift)
        print sub_shift, value
        newlist.append(value)
    #print newlist
    key = newlist.index(min(newlist))
    mychar = alp[key]
    keyword.append(mychar)
    print keyword



for i in range(0, len(sub)):
    analiz(sub[i])

key = ""
for i in range(0, len(keyword)):
    key += keyword[i]

print key

#here we expand the key
for i in range(0, len(string)):
    key += key[i]

print key
plaintext = ""
for i in range(0, len(string)):
    new = alp.index(string[i]) - alp.index(key[i]) % 26
    if new < 0 :
        new = new + 26
    plaintext += alp[new]
print plaintext
