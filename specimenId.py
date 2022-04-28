import csv

def getCatalog(file):
    with open(file) as f:
        reader = csv.reader(f)
        i = 0
        specIdCatalog = {}
        sampleIdCatalog = {}
        for row in reader:
            data = [ro.strip() for ro in row]
            if i == 0:
                samplesId = [int(x) for x in data[1:]]
                print(samplesId)
            else:
                # print(data)
                for count, item in enumerate(data[1:]):
                    if item:
                        # print('count = {}, item = {}, samplesId = {}'.format(count,item, samplesId[count]))
                        for _ in range(int(item)):
                            if samplesId[count] in sampleIdCatalog:
                                sampleIdCatalog[samplesId[count]].append(data[0])
                            else:
                                sampleIdCatalog[samplesId[count]] = [data[0],]
                        # for range(int(item)):
                        #     sampleIdCatalog[data[count]].append()
                if data[0] in specIdCatalog:
                    print("duplicate id {}".format(data))
                else:
                    specIdCatalog[data[0]] = data
            i += 1
    return sampleIdCatalog

def getInsert(specimenIdBegin,specIdCatalog,fileNameSQL):
    specimen_id = specimenIdBegin
    f = open(fileNameSQL, "w")
    for key, values in specIdCatalog.items():
        sample_id = key
        for sp_id in values:
            species_id = sp_id
            specimen_id += 1
            # print("specimen_id={},species_id={},sample_id={}".format(specimen_id,species_id,sample_id))
            # print("INSERT INTO specimen (specimen_id, species_id, sample_id) VALUES ('{}','{}','{}');".format(specimen_id,species_id,sample_id))
            f.write("INSERT INTO specimen (specimen_id, species_id, sample_id) VALUES ('{}','{}','{}');\n".format(specimen_id,species_id,sample_id))
    f.close()


# fileName = "/Users/asya/science/Database/prepared/Processed/2015rspecimen_.csv"
# fileName = "/Users/asya/science/Database/prepared/Processed/2016r_spn.csv"
# fileName = "/Users/asya/science/Database/prepared/Processed/2016kz_spn.csv"
# fileName = "/Users/asya/science/Database/prepared/Processed/2016t_spn.csv"
fileName = "/Users/asya/science/Database/prepared/Processed/specimen_id_csv_to_proc/2018t_spn.csv"
# fileName = "/Users/asya/science/Database/prepared/Processed/test1.csv"
fileNameSQL = "/Users/asya/science/Database/prepared/Processed/test.txt"

specIdCatalog = getCatalog(fileName)
# print(specIdCatalog)
getInsert(19528, specIdCatalog, fileNameSQL)
