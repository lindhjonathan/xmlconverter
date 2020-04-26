#!/usr/bin/env python3

import xml.etree.ElementTree as xml
from xml.dom.minidom import parseString

def readFile():
    filename = "to_transform.txt"
    with open(filename) as filehandle:
        line = filehandle.readlines()

    lines = [li.strip() for li in line]
    return lines

def convertToXML(lines):
    filename = "transformed.xml"
    xml_root = xml.Element("people")
    xml_root.text = "\n\t"

    for index, line in enumerate(lines):
        if lines[index][0] is "P" and not None:
            personlist = lines[index].split("|")
            xml_person = xml.Element("person")
            xml_person.text = "\n\t\t"
            xml_person.tail = "\n\t"

            xml_firstname = xml.SubElement(xml_person, "firstname")
            xml_firstname.text = personlist[1]
            xml_firstname.tail = "\n\t\t"
            xml_lastname = xml.SubElement(xml_person, "lastname")
            xml_lastname.text = personlist[2]
            xml_lastname.tail = "\n\t\t"

            nextline = index + 1
            while nextline < len(lines) and lines[nextline][0] is not "P":
                if lines[nextline][0] is "F":
                    familylist = lines[nextline].split("|")

                    xml_family = xml.SubElement(xml_person, "family")
                    xml_family.text = "\n\t\t\t"
                    xml_family.tail = "\n\t\t"
                    xml_name = xml.SubElement(xml_family, "name")
                    xml_name.text = familylist[1]
                    xml_name.tail = "\n\t\t\t"
                    xml_born = xml.SubElement(xml_family, "born")
                    xml_born.text = familylist[2]
                    xml_born.tail = "\n\t\t\t"


                    if lines[nextline+1][0] is "T":
                        phonelist = lines[nextline+1].split("|")

                        xml_phone = xml.SubElement(xml_family, "phone")
                        xml_phone.text = "\n\t\t\t\t"
                        xml_phone.tail = "\n\t\t"
                        xml_mobile = xml.SubElement(xml_phone, "mobile")
                        xml_mobile.text = phonelist[1]
                        xml_mobile.tail = "\n\t\t\t\t"
                        xml_landline = xml.SubElement(xml_phone, "landline")
                        xml_landline.text = phonelist[2]
                        xml_landline.tail = "\n\t\t\t"

                        nextline +=1

                    if lines[nextline+1][0] is "A":
                        addresslist = lines[nextline+1].split("|")

                        xml_address = xml.SubElement(xml_family, "address")
                        xml_address.text = "\n\t\t\t\t"
                        xml_address.tail = "\n\t\t"
                        xml_street = xml.SubElement(xml_address, "street")
                        xml_street.text = addresslist[1]
                        xml_street.tail = "\n\t\t\t\t"
                        xml_city = xml.SubElement(xml_address, "city")
                        xml_city.text = addresslist[2]
                        xml_city.tail = "\n\t\t\t"
                        if len(addresslist) > 3:
                            xml_city.tail = "\n\t\t\t\t"
                            xml_zip = xml.SubElement(xml_address, "zip")
                            xml_zip.text = addresslist[3]
                            xml_zip.tail = "\n\t\t\t"
                        nextline +=1

                    nextline +=1


                elif lines[nextline][0] is "A":
                    addresslist = lines[nextline].split("|")

                    xml_address = xml.SubElement(xml_person, "address")
                    xml_address.text = "\n\t\t\t"
                    xml_address.tail = "\n\t\t"
                    xml_street = xml.SubElement(xml_address, "street")
                    xml_street.text = addresslist[1]
                    xml_street.tail = "\n\t\t\t"
                    xml_city = xml.SubElement(xml_address, "city")
                    xml_city.text = addresslist[2]
                    xml_city.tail = "\n\t\t"
                    if len(addresslist) > 3:
                        xml_city.tail = "\n\t\t\t"
                        xml_zip = xml.SubElement(xml_address, "zip")
                        xml_zip.text = addresslist[3]
                        xml_zip.tail = "\n\t\t"
                    nextline += 1


                elif lines[nextline][0] is "T":
                    phonelist = lines[nextline].split("|")

                    xml_phone = xml.SubElement(xml_person, "phone")
                    xml_phone.text = "\n\t\t\t"
                    xml_phone.tail = "\n\t\t"
                    xml_mobile = xml.SubElement(xml_phone, "mobile")
                    xml_mobile.text = phonelist[1]
                    xml_mobile.tail = "\n\t\t\t"
                    xml_landline = xml.SubElement(xml_phone, "landline")
                    xml_landline.text = phonelist[2]
                    xml_landline.tail = "\n\t\t"
                    nextline += 1

                else:
                    break


            xml_person[-1].tail = "\n\t"
            xml_root.append(xml_person)

    xml_root[-1].tail = "\n"
    return xml_root

def writeXMLFile(xml_to_write):
    xml_tree = xml.ElementTree(xml_to_write)
    xml_str = xml.tostring(xml_tree.getroot(), encoding='unicode', method="xml", short_empty_elements=False)

    filename = "transformed.xml"

    with open(filename, "w+") as filehandle:
        filehandle.write(xml_str)

lines = readFile()
xml_to_write = convertToXML(lines)
writeXMLFile(xml_to_write)
