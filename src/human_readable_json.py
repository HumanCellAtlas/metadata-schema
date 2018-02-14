from optparse import OptionParser
import logging
import os
from schema_test_suite import get_json_from_file




class MarkdownGenerator:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generateMarkdown(self, schemas, entity_type):
        file = open("../docs/" + entity_type + ".md", "w")
        file.write("# " + entity_type.capitalize() + "\n")

        for path in schemas:

            schema = get_json_from_file(path)

            if (entity_type == "module" or entity_type == "core"):
                file.write("## " + schema["title"] + "<a name='" + schema["title"] + "'></a>\n")
            else:
                file.write("## " + schema["title"] + "\n")
            file.write("_" + schema["description"] + "_\n")
            file.write("\n")
            file.write("Location: " +  path.replace("../json_schema/", "") + "\n")
            file.write("\n")

            file.write("Property name | Description | Type | Required? | Module reference? | User friendly name | Allowed values | Example \n")
            # file.write("Property name | Description | Type  \n")
            file.write("--- | --- | --- | --- | --- | --- | --- | --- \n")

            required = schema["required"]

            for property in schema["properties"]:

                if "$ref" in schema["properties"][property]:
                    ref = schema["properties"][property]["$ref"]
                    if "definitions" not in ref:
                        if "core" in ref:
                            dir = "core"
                        elif "module" in ref:
                            dir = "module"
                        else:
                            dir = ""
                        mod = ref.split("/")[-1]
                        mod = mod.replace(".json", "")
                        link = "[See " + dir + "  " + mod + "](" + dir + ".md/#" + mod + ")"
                    else:
                        link = ""


                elif "items" in schema["properties"][property] and "$ref" in schema["properties"][property]["items"]:
                    ref = schema["properties"][property]["items"]["$ref"]
                    if "definitions" not in ref:
                        if "core" in ref:
                            dir = "core"
                        elif "module" in ref:
                            dir = "module"
                        else:
                            dir = ""
                        mod = ref.split("/")[-1]
                        mod = mod.replace(".json", "")
                        link = "[See " + dir + "  " + mod + "](" + dir + ".md/#" + mod + ")"
                    else:
                        link = ""
                else:
                    link = ""

                # if link is not "":
                #     print(schema["title"] + "\t "+ property + "\t"+ link)

                file.write(property + " | "+
                           (schema["properties"][property]["description"] if "description" in schema["properties"][property] else "") + " | " +
                           (schema["properties"][property]["type"] if "type" in schema["properties"][property] else "")  + " | " +
                           ("yes" if property in required else "no")  + " | " +
                           link + " | " +
                           (schema["properties"][property]["user_friendly"] if "user_friendly" in schema["properties"][property] else "") + " | " +
                           (", ".join(schema["properties"][property]["enum"]) if "enum" in schema["properties"][property] else "") + " | " +
                           (str(schema["properties"][property]["example"]) if "example" in schema["properties"][property] else "") + "\n")




            file.write("\n")


        file.close()





if __name__ == '__main__':


    generator = MarkdownGenerator()

    base_schema_path = '../json_schema'

    core_schema_path = base_schema_path + '/core'
    type_schema_path = base_schema_path + '/type'
    module_schema_path = base_schema_path + '/module'
    bundle_schema_path = base_schema_path + '/bundle'

    core_schemas = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(core_schema_path)
               for f in files if f.endswith('.json')]

    type_schemas = [os.path.join(dirpath, f)
                    for dirpath, dirnames, files in os.walk(type_schema_path)
                    for f in files if f.endswith('.json')]
    module_schemas = [os.path.join(dirpath, f)
                    for dirpath, dirnames, files in os.walk(module_schema_path)
                    for f in files if f.endswith('.json')]
    bundle_schemas = [os.path.join(dirpath, f)
                    for dirpath, dirnames, files in os.walk(bundle_schema_path)
                    for f in files if f.endswith('.json')]

    generator.generateMarkdown(core_schemas, "core")
    generator.generateMarkdown(type_schemas, "type")
    generator.generateMarkdown(module_schemas, "module")
    generator.generateMarkdown(bundle_schemas, "bundle")







""""
steps:
1. read in schemas
2. for each schema, 
"""