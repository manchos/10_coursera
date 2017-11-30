# Coursera Dump

[TODO. There will be project description]

# Project Goals


Displays 20 random courses from https://www.coursera.org/ and output information to xlsx file.


The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


# Using

Run the script
```#!bash
$ python coursera.py


optional arguments:
  -h, --help            show this help message and exit
  -cachetime CACHE_TIME set cache time interval
  -clearcache           clear cache file
```

and save courses to xlsx file like this:

   COURSE NAME	   | URL ADDRESS	| LANGUAGE	| START DATE | WEEKS DURATION |	RATING |
-------------------|----------------|-----------|------------|----------------|--------|
Positive Psychology|https://www.coursera.org/learn/positive-psychology|English|	18.12.2017|	6|	4.6|



# Requirement

Python >= 3.5

requests==2.11.1

openpyxl==2.4.7

beautifulsoup4==4.6.0
