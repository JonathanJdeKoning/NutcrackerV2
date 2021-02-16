import random
import sys
import time
import base64
import os
os.system("clear")

print("""            _.-O-._
           o_o_o_o_o
           \_`___`_/
           } /. .\ {
          } | _c_ | {
         __}_\www/_{__
        ((((  { }  ))))
         | |o { } o| |
         | |o {_} o| |
         |_\o  _  o/_|
         \_/==L_I//\_/
          \)-.__//-(/
           | : //: |
           | :|/ : |
           | : | : |
           | : | : |
           |---|---|
           |__ | __|
           (___|___)""")
print("""             _                      _             
            | |                    | |            
 _ __  _   _| |_ ___ _ __ __ _  ___| | _____ _ __ 
| '_ \| | | | __/ __| '__/ _` |/ __| |/ / _ \ '__|
| | | | |_| | || (__| | | (_| | (__|   <  __/ |   
|_| |_|\__,_|\__\___|_|  \__,_|\___|_|\_\___|_| """)

lowerstr = "welcome to the nutcracker"
upperstr = lowerstr.upper()
for x in range (len(lowerstr)):
	s = lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
	sys.stdout.write(s)
	sys.stdout.flush()
	time.sleep(0.075)
print("\r")
nut = input("NUT: ")


choice = input("""\nChoose an one or more options. For multiple operations, separate by spaces. \nFor compound operations, separate by commas:\n
All:            0
ENCRYPTION:
    Text to Binary: 1
    Text to Ascii:  2
    Text to Hex:    3
    Text to Octal:  4
    Text to Base64: 5
    Text to A1Z26:  6
    Atbash:         7
    Text to MD5:    8
    Text to Uncle:  9    
DECRYPTION:
    Binary to Text:10
    Ascii to Text: 11
    Hex to Text:   12
    Octal to Text: 13
    Base64 to Text:14
    A1Z26 to Text: 15
    Uncle to Text: 16
MANIPULATION:
    ROT:           17
    Reverse:       18
    To Upper:      19
    To Lower:      20
    Switch Case:   21
    To Pig Latin:  22

>> """)

def text_to_binary(s):
	res = ' '.join(format(ord(i), 'b') for i in s)
	global nut
	nut = res
	return res


def text_to_ascii(s):
	new = ""
	for c in s:
		new += str(ord(c)) + " "
	global nut
	nut = new
	return new


def text_to_hex(s):
	new = ""
	for c in s:
		new += c.encode("utf-8").hex() + " "
	global nut
	nut = new
	return new


def text_to_octal(s):
	new = ""
	for c in s:
		new += oct(ord(c))[2:] + " "
	global nut
	nut = new
	return new


def text_to_base64(s):
	s_bytes = s.encode("ascii")
	b64_bytes = base64.b64encode(s_bytes)
	new = b64_bytes.decode("ascii")
	global nut
	nut = new
	return new


def text_to_A1Z26(s):
	new = ""
	for c in s:
		if c.isalpha():
			new += str(ord(c)-96) + " "
	global nut
	nut = new
	return new


def text_to_atbash(s):
	lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A', 'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v', 
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q', 
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l', 
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g', 
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'} 

	cipher = '' 
	for letter in s: 
		if letter.isalpha():
			cipher += lookup_table[letter] 
		else: 
			cipher += letter 
	global nut
	nut = cipher
	return cipher 


def text_to_MD5(s):
    os.system("touch "+ s + "> /dev/null")
    os.system("echo " + s + " > " + s)
    print("\n\n")
    os.system("md5sum " + s)
    os.system("rm " + s + " > /dev/null")
    return("")
		# ADD GLOBAL NUT THINGY


def uncle(s):
    ones = ['A','E','F','H','I','K','L','M','N','T','V','W','X','Y','Z']
    zeros = ['B','C','D','G','J','O','P','Q','R','S','U']
    new = "" 
    for c in s.upper():
        if c.isalpha():
            new += format(ord(c), 'b')[2:] + " "
        elif c == " ":
            new += "%%"

    newer = ""
    for c in new:
        if c == "1":
            ran = int(random.randint(0,len(ones)-1))
            newer += ones[ran]
        elif c == "0":
            ran = int(random.randint(0,len(zeros)-1))
            newer += zeros[ran]
        elif c == " ":
            newer += str(random.randint(1,9))
        elif c == "%%":
            newer += str(random.randint(10,99))
        global nut
        nut = newer    
        return newer


def binary_to_text(s):
		s = s.replace(" ", "")
		nut = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
		return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


def ascii_to_text(s):
    global nut
    nut = ''.join(chr(int(i)) for i in s.split())
    return ''.join(chr(int(i)) for i in s.split())

def hex_to_text(s):
    s = s.replace(" ", "")
    global nut
    nut = bytearray.fromhex(s).decode()
    return bytearray.fromhex(s).decode()


def octal_to_text(s):
	str_converted = ""
	for octal_char in s.split(" "):
		try:
			str_converted += chr(int(octal_char, 8))
		except ValueError:
			return "ERROR: REMOVE SPACE AT END OF STRING"
	global nut
	nut = str_converted
	return str_converted

def b64_to_text(s):
	base64_bytes = s.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	global nut
	nut = message_bytes.decode('ascii')
	return message_bytes.decode('ascii')


def A1Z26_to_text(s):
	string = ""	
	data = s.split()
	
	for char in data:	
		char = chr(int(char) + 96)
		string += char
	global nut
	nut = string	
	return(string)		
	

def uncle_to_text(s):
    ones = ['A','E','F','H','I','K','L','M','N','T','V','W','X','Y','Z']
    zeros = ['B','C','D','G','J','O','P','Q','R','S','U']  

    new = "11"

    for c in s:
        if c in ones:
            new+="1"
        elif c in zeros:
            new+="0"
        elif c in "123456789":
            new+=" 11"
    new = new[:-2]
    global nut
    nut = ''.join(chr(int(new[i*8:i*8+8],2)) for i in range(len(new)//8))
    return ''.join(chr(int(new[i*8:i*8+8],2)) for i in range(len(new)//8))


def rot(s):
	final = ""
	for i in range(1, 26):
		loop_point = 26-i+1
		new = ""
		for c in s:
			if c.isupper():
				number = ord(c) - 64
			elif c.islower():
				number = ord(c) - 96
			else: 
				number = 0
			
			if number < loop_point and c.isalpha():
				new += chr(ord(c)+i)
			elif number >= loop_point and c.isalpha():
				new += chr(ord(c)- (26 - i))
			else:
				new += c
		final += f"\nROT {i}: {new}" #IF YOU'RE READING THIS, USE PYTHON 3
	
	return final


def rev(s):
    global nut
    nut = s[::-1]
    return s[::-1]


def toupper(s):
    global nut
    nut = s.upper()
    return s.upper()


def tolower(s):
    global nut
    nut = s.lower()
    return s.lower()


def switch_case(s):
    new = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                new += c.upper()
            elif c.isupper():
                new+= c.lower()
        else:
            new+=c
    global nut
    nut = new
    return new
        

def latin(s):
    new = ""
    for c in s:
        if c != " ":
            if not c.isalpha():
                s = s.replace(c,"")
            
    s_array = s.split()

    for item in s_array:
        vowel_position = 0
        for c in item:
            if c not in "aeiouy":
                vowel_position += 1
            elif c in "aeiouy" and vowel_position == 0:
                new += item + "yay "
                break
            elif c in "aeiouy" and vowel_position > 0:
                new += item[vowel_position:] + item[:vowel_position] + "ay "
                break
    global nut
    nut = new        
    return new


choice = choice.split()
choice_array = choice
print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~")
for i in range(len(choice_array)):
    choice = choice_array[i]
    print("\n\n" + text_to_binary(nut)) if choice == "1" else None
    print("\n\n" + text_to_ascii(nut))  if choice == "2" else None
    print("\n\n" + text_to_hex(nut))    if choice == "3" else None
    print("\n\n" + text_to_octal(nut))  if choice == "4" else None
    print("\n\n" + text_to_base64(nut)) if choice == "5" else None
    print("\n\n" + text_to_A1Z26(nut))  if choice == "6" else None
    print("\n\n" + text_to_atbash(nut)) if choice == "7" else None
    print(""+text_to_MD5(nut))          if choice == "8" else None
    print("\n\n" + uncle(nut))          if choice == "9" else None
    print("\n\n" + binary_to_text(nut)) if choice =="10" else None
    print("\n\n" + ascii_to_text(nut))  if choice =="11" else None
    print("\n\n" + hex_to_text(nut))    if choice =="12" else None
    print("\n\n" + octal_to_text(nut))  if choice =="13" else None
    print("\n\n" + b64_to_text(nut))    if choice =="14" else None
    print("\n\n" + A1Z26_to_text(nut))  if choice =="15" else None
    print("\n\n" + uncle_to_text(nut))  if choice =="16" else None
    print("\n\n" + rot(nut))            if choice =="17" else None
    print("\n\n" + rev(nut))            if choice =="18" else None
    print("\n\n" + toupper(nut))        if choice =="19" else None
    print("\n\n" + tolower(nut))        if choice =="20" else None
    print("\n\n" + switch_case(nut))    if choice =="21" else None
    print("\n\n" + latin(nut))          if choice =="22" else None

print("\n\n~_~_~_~_~_~_~_~_~_~_~_~_~_~_~")



