#!/bin/bash

username="****"
password="****"
echo
curl -u $username:$password --silent "https://mail.google.com/mail/feed/atom" > test.xml