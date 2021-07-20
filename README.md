# rdns-find

Performs reverse DNS lookups given a file of CIDR and/or regular IP addresses<br>
Must specify input and output files<br>
Outputs csv<br>
<br>
EXAMPLE USAGE:<br>
```./rdns-find.py -i addresses.txt -o rdns.csv```<br>
<br>
SAMPLE OUTPUT:
```
['159.8.65.120'],78.41.089f.ip4.static.sl-reverse.com

['159.8.65.121'],79.41.089f.ip4.static.sl-reverse.com

['159.8.65.122'],7a.41.089f.ip4.static.sl-reverse.com
```
