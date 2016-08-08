#!/bin/bash
nohup java -jar selenium-server-standalone-2.34.0.jar  -role hub > /dev/null &
nohup ./bin/phantomjs --webdriver=8080 --webdriver-selenium-grid-hub=http://127.0.0.1:4444 > /dev/null &
