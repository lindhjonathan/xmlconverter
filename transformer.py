#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Kika på att skapa executable av pyscript: http://www.py2exe.org/

def readFile():
    filename = "to_transform.txt"
    with open(filename) as filehandle:
        line = filehandle.readlines()

    lines = [li.strip() for li in line]
    return lines

def convertToXML(lines):
    xml = ""

    for line in lines:
        if line[0] is "P":
            print(line)

    return "dummy"

def writeXMLFile(xml):
    filename = "transformed.xml"
    with open(filename, "w+") as filehandle:
        for line in xml:
            filehandle.write("%s\n" % line)

text = readFile()
xml = convertToXML(text)
writeXMLFile(xml)

print(xml)
