from optparse import OptionParser
import logging
import openpyxl



class SpreadsheetCreator:


    def __init__(self, dry=False, output=None, schema_version=None):
        print("foo")




if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--schema", dest="schema_uri",
                      help="Base schema URI for the metadata")
    parser.add_option("-o", "--output", dest="output",
                      help="Output directory where to dump json files submitted to ingest", metavar="FILE", default=None)
    parser.add_option("-v", "--version", dest="schema_version", help="Metadata schema version", default=None)


    (options, args) = parser.parse_args()
    if not options.path:
        print ("You must supply path to the HCA bundles directory")
        exit(2)
    # submission = SpreadsheetSubmission(options.dry, options.output, options.schema_version)
    # submission.submit(options.path, None, None, options.project_id)



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