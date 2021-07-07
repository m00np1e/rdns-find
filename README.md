# rdns-find

Performs reverse DNS lookups given a file of CIDR and/or regular IP addresses<br>
Must specify input and output files<br>
<br>
EXAMPLE USAGE:<br>
```./rdns-find.py -i addresses.txt -o rdns.txt```<br>
<br>
SAMPLE OUTPUT:<br>
```IP Address    RDNS
192.168.0.1 - test.com
192.168.0.2 - test2.com
```
