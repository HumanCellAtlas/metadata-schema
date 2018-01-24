from optparse import OptionParser
import logging
import openpyxl
from openpyxl import Workbook
import requests, pprint



class SpreadsheetCreator:


    def __init__(self, dry=False, output=None, schema_version=None):
        self.logger = logging.getLogger(__name__)

    def generateSpreadsheet(self, pathToSchemas, output):
        values = []
        try:
            for schema in pathToSchemas:
                v = self._gatherValues(schema)
                values.append(v)

                # values.append(self._gatherValues(schema))

            self._buildSpreadsheet(values, output)
        except ValueError as e:
            self.logger.error("Error:" + str(e))
            raise e

    def _gatherValues(self, schema):


        req = requests.get(schema)

        if (req.status_code == requests.codes.ok):
            jsonRaw = req.json()

            pp = pprint.PrettyPrinter(indent=4)

            entities = []

            entity_title = jsonRaw["title"]


            properties = jsonRaw["properties"]

            values = []

            for prop in properties:
                if ("user_friendly" in properties[prop]):
                    # pp.pprint(properties[prop]["user_friendly"])
                    if ("description" in properties[prop]):
                      # pp.pprint(properties[prop]["description"])
                      values.append({"header":properties[prop]["user_friendly"], "description":properties[prop]["description"]})
                elif("$ref" in properties[prop]):
                    module = properties[prop]["$ref"]
                    module_values = self._gatherValues(module)
                    entities.append(module_values)

                elif("items" in properties[prop] and "$ref" in properties[prop]["items"]):
                    module = properties[prop]["items"]["$ref"]
                    module_values = self._gatherValues(module)
                    entities.append(module_values)

            entities.append({entity_title : values})
        else:
            print(schema + " does not exist")

        return entities


    def _buildSpreadsheet(self, values, outputLocation):
        wb = Workbook()

        for entity in values:
            titles = entity.keys

            for entity_title in titles:

                headers = entity[entity_title]

                ws = wb.create_sheet(title=entity_title)
                col = 1

                for header in headers:
                    ws.cell(column=col, row=1, value=header["description"])
                    ws.cell(column=col, row=2, value=header["header"])
                    col =+1

        wb.save(filename=outputLocation)


if __name__ == '__main__':
    # parser = OptionParser()
    # parser.add_option("-s", "--schema", dest="schema_uri",
    #                   help="Base schema URI for the metadata")
    # parser.add_option("-o", "--output", dest="output",
    #                   help="Output directory where to dump json files submitted to ingest", metavar="FILE", default=None)
    #
    #
    # (options, args) = parser.parse_args()
    # if not options.path:
    #     print ("You must supply path to the HCA bundles directory")
    #     exit(2)
    # submission = SpreadsheetSubmission(options.dry, options.output, options.schema_version)
    # submission.submit(options.path, None, None, options.project_id)


    generator = SpreadsheetCreator()
    generator.generateSpreadsheet(["https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/v5_prototype/json_schema/type/biomaterial/organism.json"], "spreadsheet_test.xlsx")

        # - base
        # schema
        # URI - required
        # - entities
        # to
        # convert
        # to
        # s / sheet - optional, convert
        # all
        # entites
        # - schema
        # version
        # of
        # each
        # entity - optional?
        # - output
        # file
        # name / path - required