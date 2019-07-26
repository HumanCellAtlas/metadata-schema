import csv
import datetime
import os

from version_update import VersionUpdater
import human_readable_json



class ReleasePrepare:
    def __init__(self):
        self.srcfolder = os.getcwd()
        foldername = os.path.basename(self.srcfolder)
        self.schemafolder = self.srcfolder.replace(foldername,"json_schema")

    def openUpdateLog(self):
        update_log = self.schemafolder + "/update_log.csv"
        with open(update_log, 'r') as readFile:
            reader = csv.reader(readFile)
            log_content = list(reader)

            header = log_content[0]
            self.setColumnIndexes(header)
        readFile.close()
        return log_content

    def setColumnIndexes(self, header):
        for index, h in enumerate(header):
            if h == 'Version':
                self.version_column = index
            elif h == 'Date':
                self.date_column = index
            elif h == 'Schema':
                self.schema_column = index
            elif h == 'Change type':
                self.type_column = index
            elif h == 'Change message':
                self.message_column = index


    def updateVersions(self, log_content):
        # find any row where the version column is empty and increment the version number
        # using the version_update script and log parameters

        migrationUpdates = {}

        for val in range(1, len(log_content)):
            #generate a list of independent schemas from the update log
            independent_schemas = []
            for v in range(1, len(log_content)):
                independent_schemas.append(log_content[v][self.schema_column])

            if not log_content[val][self.version_column]:
                schema = log_content[val][self.schema_column]
                change_type = log_content[val][self.type_column]
                version_options = options(self.schemafolder, schema,change_type,independent_schemas)
                versionUpdater = VersionUpdater(version_options)
                versionUpdates = versionUpdater.updateVersions(True)

                for key in versionUpdates.keys():
                    if key == schema:
                        log_content[val][self.version_column] = versionUpdates[key]
                        migrationUpdates[schema.split("/")[-1]] = versionUpdates[key]
                    else:
                        # add dependeny updates to the update log
                        new_row = log_content[val].copy()
                        new_row[self.version_column] = versionUpdates[key]
                        new_row[self.schema_column] = key
                        log_content.append(new_row)
                        migrationUpdates[key.split("/")[-1]] = versionUpdates[key]

        versionUpdater.updateMigrations(migrationUpdates)

        return log_content

    # build the change log content from the structured update log file
    def buildChangeLog(self, log_content):
        now = datetime.datetime.now()
        update_date = now.strftime("%Y-%m-%d")

        log_insert = ''
        # find any row where the date column is empty and include it in the changelog markdown file
        for val in range(1, len(log_content)):
            if not log_content[val][self.date_column]:
                log_content[val][self.date_column] = update_date
                schema = log_content[val][self.schema_column]
                change_message = log_content[val][self.message_column]
                version = log_content[val][self.version_column]
                type = change_message.split(' ')[0]

                markdown_message = "### [" + schema + ".json - v" + version + "] - " + update_date + "\n" + "### " + type  + "\n" + change_message  + "\n"
                log_insert = log_insert + markdown_message  + "\n"

        output = self._buildLogOutput(log_insert)
        self._saveChangeLog(output)
        self._saveUpdateLog(log_content)


    # build the actual changelog.md file by putting the change log statements in log_insert below the [Unreleased]... line
    def _buildLogOutput(self, log_insert):
        change_log_file = self.schemafolder.replace("json_schema", "") + "/changelog.md"
        output = ""
        with open(change_log_file, 'r') as readChangeLog:
            log = readChangeLog.readlines()
            ignoreNextLine = False
            for line in log:
                if "## [Unreleased](https://github.com/HumanCellAtlas/metadata-schema/tree/develop)" in line:
                    output = output + line + "\n"
                    output = output + log_insert
                    ignoreNextLine = True
                else:
                    if ignoreNextLine:
                        ignoreNextLine = False
                    else:
                        output = output + line
        readChangeLog.close()
        return output

    def _saveChangeLog(self, output):
        change_log_file = self.schemafolder.replace("json_schema", "") + "/changelog.md"
        with open(change_log_file, 'w') as writeChangeLog:
            writeChangeLog.write(output)
        writeChangeLog.close()

    def _saveUpdateLog(self, output):
        # Save only the header row back to the upldate_log file
        change_log_file = self.schemafolder + "/update_log.csv"
        h = output[0]
        with open(change_log_file, 'w') as writeChangeLog:
            writer = csv.writer(writeChangeLog)
            writer.writerow(h)
        writeChangeLog.close()

    def checkUpdateLog(self, update_log):
        for val in range(1, len(update_log)):
            change_message = update_log[val][self.message_column]
            type = change_message.split(' ')[0]
            if type not in ['Added', 'Changed', 'Removed', 'Fixed', 'Deprecated', 'Security']:
                print(
                    "WARNING: Change type in log message does not match one of 'Added', 'Changed', 'Removed', 'Fixed', 'Deprecated', 'Security'")
                exit(2)

class options:
    def __init__(self, p, s, i, e):
        self.path = p
        self.schema = s
        self.increment_type = i
        self.exclude = e


if __name__ == '__main__':

    releasePrep = ReleasePrepare()

    content_log = releasePrep.openUpdateLog()

    releasePrep.checkUpdateLog(content_log)

    updated_versions = releasePrep.updateVersions(content_log)

    updated_dates = releasePrep.buildChangeLog(updated_versions)





