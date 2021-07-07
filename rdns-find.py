#!/usr/bin/env python3

import socket
import ipaddress
import csv
import argparse


# Performs reverse DNS lookups given a file of cidr and/or regular ip addresses
# Input file must be delimited by a new line
# Output file contains IP address and reverse DNS name, one per line
# Ken Mininger, July 2021
# kmininger@us.ibm.com


# get arguments
def check_args():
    parser = argparse.ArgumentParser(
        description="Performs reverse DNS lookups given a file of cidr and/or regular ip addresses",
        prog="./rdns-find.py", usage="%(prog)s "
                                     "[options]")
    parser.add_argument("-i", help="Input file", required=True)
    parser.add_argument("-o", help="Output file", required=True)
    args1 = parser.parse_args()
    return (args1)


# open output file
def open_output_file(outfile):
    try:
        open(outfile, "w")
        print("Opened", outfile, "for writing")
    except IOError:
        print("Error: Cannot open output file for writing")


# get the rdns
def rev_dns(infile, outfile):
    try:
        print("IP Address     RDNS")
        print("IP Address     RDNS", file=open((outfile), "a"))
        with open(infile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\n')
            for row in csv_reader:
                if any("/" in word for word in row):
                    addresses = [str(ip) for ip in ipaddress.IPv4Network(row[0])]
                else:
                    addresses = row
                add_len = len(addresses)
                x = 0
                while x < add_len:
                    name, alias, addresslist = socket.gethostbyaddr(addresses[x])
                    new_addr = ""
                    print((new_addr.join(addresslist)), "-", name, file=open((outfile), "a"))
                    print((new_addr.join(addresslist)), "-", name)
                    x += 1
    except IOError:
        print("Error: Cannot open input file for reading or input file not found")


# main
def main():
    # get arguments
    (args) = check_args()

    # open output file
    open_output_file(args.o)

    # do the stuff
    rev_dns(args.i, args.o)


if __name__ == '__main__':
    main()
