import os

def CreateDictionary():
    # We want to create a dictionary to number and list out all of our values i.e patient annotation details
    Input = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
    FileList = []
    FileDict = {}
    for root, dirs, filenames in os.walk(Input):
        # Create a number assigned to each filename in list for auto assigned tasks later on
        for counter, value in enumerate(filenames):
            # editing a directory properly that is indexed correctly in the list that it is
            Location_File = root + '/' + filenames[counter]

            FileList.append(Location_File)

            with open(FileList[counter]) as file:
                lines = file.readlines()
                try:
                    FileDict[counter].append(lines)
                except KeyError:
                    FileDict[counter] = [lines]

