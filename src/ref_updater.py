from optparse import OptionParser
import os, json


def update_refs(args):
    url = args.url
    input = args.input
    output = args.output


    files = getJsonFiles(input)

    for f in files:
        if ".json" in f:
            updateJson(input, f, output, url)

def updateJson(input, f, output, url):
    with open(f) as data_file:
        jsonData = json.load(data_file)
        newJson = replaceUrl(jsonData, "$ref", url)
        dumpJsonToFile(output, newJson, f)


def dumpJsonToFile(outputDir, object, name):
    if outputDir:
        dir = os.path.abspath(outputDir)
        if not os.path.exists(dir):
            os.makedirs(dir)
        tmpFile = open(dir + "/" +name, "w")
        tmpFile.write(json.dumps(object, indent=4))
        tmpFile.close()


def replaceUrl(jsonSchema, k, v):
    for key in jsonSchema.keys():
        if key == k:
            old = jsonSchema[key]
            jsonSchema[key] = v + old
        elif type(jsonSchema[key]) is dict:
            replaceUrl(jsonSchema[key], k, v)

    return jsonSchema




def getJsonFiles(path):
    if os.path.exists(path):
        # filesInDir = os.listdir(path)


        filesInDir = [os.path.join(dirpath, f)
     for dirpath, dirnames, files in os.walk(path)
     for f in files if f.endswith('.json')]
        return filesInDir


    else:
        print(path + " is not a valid directory")
        exit(3)



if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Full reference URL")
    parser.add_option("-i", "--input", dest="input", help="Path to json files")
    parser.add_option("-o", "--output", dest="output", help="Path for outout json")

    (options, args) = parser.parse_args()
    if not options.url:
        print("You must supply a full URL")
        exit(2)

    update_refs(options)