#!/bin/sh
touch ./ipaddr.text
ifconfig  >> ./ipaddr.text
scp ./ipaddr.text NAS:/home/keanu/
rm ./ipaddr.text
