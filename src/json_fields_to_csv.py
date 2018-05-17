from optparse import OptionParser
import logging
import os
from schema_test_suite import get_json_from_file


class CSVGenerator:

    def __init__(self):
        self.logger = logging.getLogger(__name__)


    def generateCSV(self, schemas):
        file = open("../docs/jsonBrowser/json_fields.csv", "w")

        file.write("Property,UserFriendlyName,Description,Schema,Required?\n")

        for path in schemas:
            schema = get_json_from_file(path)

            required = []

            if "required" in schema:
                required = schema["required"]


            for property in schema["properties"]:

                file.write(property + "," +
                      ("\"" +schema["properties"][property]["user_friendly"] +"\"" if "user_friendly" in schema["properties"][property] else "N/A") + "," +
                      ("\"" + schema["properties"][property]["description"] + "\"" if "description" in schema["properties"][property] else "N/A") + "," +
                       schema["title"] + "," +
                        ("1" if property in required else "0")  + "\n")


        file.close()



if __name__ == '__main__':


    generator = CSVGenerator()

    base_schema_path = '../json_schema'

    schemas = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(base_schema_path)
               for f in files if f.endswith('.json') and not f.endswith('versions.json')]



    generator.generateCSV(schemas)



