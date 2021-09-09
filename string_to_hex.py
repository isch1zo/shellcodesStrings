import sys,argparse

def opcode(stringo):
    string = stringo[::-1]
    if len(string)%4 == 0:
        print("[+] String is dividable to 4 great!")
    else:
        print("[-] String is not dividable to 4,so it may give false positive results or null bytes")
    opcodes = []
    for i in range(0, len(string), 4):
        byte = string[i:i+4]
        byte = byte.encode('utf-8')
        opcodes.append(byte.hex())
    return opcodes

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Tool to generate hex from strings for x86 shellcodes')
	parser.add_argument('-p', '--push', dest='push', action='store_true', help='To get result with push instruction')
	parser.add_argument('-s', '--string', dest='string', type=str, help='String to convert it to hex')
	args = parser.parse_args()

	if args.string:
		opcodes = opcode(args.string)
		if args.push:
    	    for i in opcodes:
        		print("push 0x"+i)
		else:
    	    for i in opcodes:
        	    print("0x"+i)
