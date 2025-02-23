#!/usr/bin/python3

import hashlib
import argparse

#Configuration
parser = argparse.ArgumentParser()
parser.add_argument('file', help="You need to pass the file to hash the content inside of it.")
parser.add_argument('-H', '--hash', help="Select the type of hash you want (Default: MD5). Types: [ 1 - MD5 | 2 - SHA1 | 3 - SHA256 | 4 - SHA512 ]", type=int,default=1)
parser.add_argument('-o', '--output', help="Export the output to a file.")
args = parser.parse_args()

def hashes(val, passw):
	match val:
		case 1:
			enc = hashlib.md5(passw).hexdigest()
			return enc
		case 2:
			enc = hashlib.sha1(passw).hexdigest()
			return enc

		case 3:
			enc = hashlib.sha256(passw).hexdigest()
			return enc

		case 4:
			enc = hashlib.sha512(passw).hexdigest()
			return enc
		case _:
			print("You need to pass a valid type of hash.\nSee: toHash.py -h")
			return 1


def main():	
	try:
		file = open(args.file, "r")
		output_file = open(args.output, "w") if args.output else None

		for passw in file:
			passw = passw.strip('\n').encode()
			enc = hashes(args.hash, passw)
			if(enc==1):
				break
			print(f"{passw.decode('ascii')}\r\t\t{enc}")
			if output_file:
				output_file.write(f"{passw.decode('ascii')}\r\t\t{enc}\n")

		if output_file:
			output_file.close()
	
	except FileNotFoundError:
		print(f"\nThe file {args.file} wasn't found in this directory.")
		return 1


main()
