from os import listdir
import os
# import glob
#
# for filename in glob.iglob('/foobar/*.txt'):
#      print('/foobar/%s' % filename)

from pathlib import Path

Input = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
FileList = []
for root, dirs, filenames in os.walk(Input):
        for f in filenames:
            Location_File = root + '/' + f
            FileList.append(Location_File)
            for counter, value in enumerate(FileList):
                print(counter, value)
        for n in FileList.index([Location_File]):
            with open(FileList[n]) as file:
                lines = file.readlines()
                # for Output in lines:

        log = open(Input + '/' + f, 'r')


def Crosscheck(Input, Output):
    Input = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
    FileList = []
    for root, dirs, filenames in os.walk(Input):
        for r in root:
            for f in filenames:
                Location_File = r + '/' + f
                FileList.append(r + '/' + f)
                with open(r + '/' +f) as file:
                    lines = file.readlines()
                    # for Output in lines:
Crosscheck("/Users/pc/Downloads/MontgomerySet/ClinicalReadings", "Yes")
