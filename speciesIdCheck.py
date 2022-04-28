import csv

def getCatalog(file):
    with open(file) as f:
        reader = csv.reader(f)
        i = 0
        # specIdCatalog = {'26': ['26', 'Staurophora', 'celsia']}
        specIdCatalog = {}
        for row in reader:
            if i != 0:
                # print("row[ufeff] = [{}] type={}".format(row[0], type(row[0])))
                data = [ro.strip() for ro in row]
                if data[0] in specIdCatalog:
                    print("duplicate id {}".format(data))
                else:
                    specIdCatalog[data[0]] = data
            # print("row[{}] = [{}] type={}, row[0] = {}".format(i, row, type(row), row[0]))
            i += 1
    # fileSpecies = open(file)
    # lines = fileSpecies.readlines()
    # a = lines[0]
    # print("a = {}".format(a))
    
    
    # for line in lines:
    #     # specIdCatalog[line[0]] = [line[1],line[2]]
    #     print("line[{}] = [{}] type={}".format(i, line, type(line)))
    #     i += 1
    return specIdCatalog

def compareNames(str1, str2):
    if str1 != str2:
        print("{}\n{}".format(str1,str2))


def checkErrs(spec_id, work_id):
    if spec_id[1:] != work_id[2:]:
        print("R-----", spec_id, work_id)
        compareNames(spec_id[1], work_id[2])
        compareNames(spec_id[2], work_id[3])
        return False
    return True

def main():
    print("main")
    catalog = getCatalog("/Users/asya/science/Database/prepared/Processed/species_id.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2015r.csv")
    checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2016r.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2016kz.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2016t.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2017r.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2017kz_.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2017j.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2018r.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2018kz.csv")
    # checkCatalog = getCatalog("/Users/asya/science/Database/prepared/Processed/2018t.csv")
    # checkCatalog["284"] = ['163', 'Diachrysia', 'stenochrysisQ']
    print("checkCatalog = {}".format(checkCatalog))

    # print("base={}".format(catalog["284"]))
    # print("check={}".format(checkCatalog["284"]))
    print("=====================")
    # noErr = checkErrs(catalog['3'], checkCatalog['3'])
    # print("noErr={}".format(noErr))
    for species in checkCatalog:
        checkErrs(catalog[species],checkCatalog[species])


main()
