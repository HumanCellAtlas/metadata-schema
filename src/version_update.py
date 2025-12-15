import collections
import json
import os
import datetime

from optparse import OptionParser


class VersionUpdater:

    def __init__(self, options=None):
        if "~" in options.path:
            self.path = os.path.expanduser(options.path)
        else:
            self.path = options.path

        self.schema_to_update = []

        if "," in options.schema:
            self.schema_to_update = options.schema.split(",")
        else:
            self.schema_to_update.append(options.schema)

        self.update_type = options.increment_type
        self.versions = self._getJson(self.path + "/versions.json")

        if options.exclude:
            self.exclude = options.exclude

    def updateVersions(self, versionTracker=False):

        toUpdate = []

        for schema in self.schema_to_update:
            ref = schema + ".json"
            toUpdate.append(schema)
            toUpdate.extend(self._findDependentSchemas(ref))

            for s in toUpdate:
                if s != schema:
                    toUpdate.extend(self._findDependentSchemas(s + ".json"))

        toUpdate = list(set(toUpdate))

        versionJson = self.versions

        updatedVersion = {}
        for s in toUpdate:
            old_version = self._findSchemaVersion(s)
            new_version = self.incrementVersion(old_version, self.update_type)

            updatedVersion[s] = new_version

            for part in reversed(s.split('/')):
                new_version = {part: new_version}

            self._update(versionJson["version_numbers"], new_version)

        now = datetime.datetime.now()

        versionJson["last_update_date"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")

        # self._saveJson(self.path, versionJson)
        self._saveJson(self.path + "/versions.json", versionJson, True)

        if versionTracker:
            return updatedVersion

    def _update(self, d, u):
        for k, v in u.items():
            if isinstance(v, collections.abc.Mapping):
                d[k] = self._update(d.get(k, {}), v)
            else:
                d[k] = v
        return d

    def _findSchemaVersion(self, schema):
        hierarchy = schema.split("/")

        latest = self.versions["version_numbers"]

        for e in hierarchy:
            latest = latest[e]

        if not isinstance(latest, dict):
            return latest


    def _getJson(self, path):
        f = open(path, 'r')
        return json.loads(f.read())

    def _saveJson(self, path, data, sort):
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=sort)


    def find(self, key, dictionary):
        for k, v in dictionary.items():
            if k == key:
                yield v
            elif isinstance(v, dict):
                for result in self.find(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    if isinstance(d, dict):
                        for result in self.find(key, d):
                            yield result


    def incrementVersion(self, version, increment_type):

        elements = version.split(".")

        if increment_type == "patch":
            inc = int(elements[2])
            new_inc = inc + 1
            elements[2] = str(new_inc)

        elif increment_type == "minor":
            inc = int(elements[1])
            new_inc = inc + 1
            elements[1] = str(new_inc)
            elements[2] = "0"

        elif increment_type == "major":
            inc = int(elements[0])
            new_inc = inc + 1
            elements[0] = str(new_inc)
            elements[1] = "0"
            elements[2] = "0"

        new_version = ".".join(elements)

        return new_version

    # find all schemas that reference "ref" as they will also need a version increment
    def _findDependentSchemas(self, ref):
        schemas = [os.path.join(dirpath, f)
                   for dirpath, dirnames, files in os.walk(self.path)
                   for f in files if f.endswith('.json') and not f.endswith('versions.json')]

        dependencies = []

        for s in schemas:
            # if "type" in s or "module" in s or "bundle" in s:
            json = self._getJson(s)

            for item in self.find("$ref", json):
                if ref == item:
                    d = s.replace(self.path+"/", "")
                    d = d.replace(".json", "")
                    if d not in dependencies and d not in self.exclude:
                        dependencies.append(d)
        return dependencies

    # update any empty version numbers in the property_migrations.json file
    def updateMigrations(self, updatedVersions):
        migrationJson =  self._getJson(self.path + "/property_migrations.json")

        for migration in migrationJson['migrations']:
            if 'effective_from' in migration and migration['effective_from'] == '':
                if migration['source_schema'] in updatedVersions.keys():
                    migration['effective_from'] = updatedVersions[migration['source_schema']]

            elif 'effective_from_source' in migration and migration['effective_from_source'] == '':
                if migration['source_schema'] in updatedVersions.keys():
                    migration['effective_from_source'] = updatedVersions[migration['source_schema']]
                if migration['target_schema'] in updatedVersions.keys():
                    migration['effective_from_target'] = updatedVersions[migration['target_schema']]

        self._saveJson(self.path + "/property_migrations.json", migrationJson, False)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="path",
                      help="Base path to the HCA metadata schemas", metavar="FILE")
    parser.add_option("-s", "--schema", dest="schema",
                      help="Schemas that were changed")
    parser.add_option("-i", "--increment_type", dest="increment_type",
                      help="The type of change that was made. Must be one of patch, minor or major.")
    parser.add_option("-e", "--exclude", dest="exclude",
                      help="List of schemas to exclude from this version update.")

    (options, args) = parser.parse_args()

    if not options.path:
        print("You must supply the path to the metadata schema directory")
        exit(2)
    if not options.schema:
        print("You must supply a schema to update")
        exit(2)
    if not options.increment_type or options.increment_type not in ["patch", "minor", "major"]:
        print("You must supply the type of change that was made and it must be one of patch, minor or major.")
        exit(2)

    versionUpdater = VersionUpdater(options)

    versionUpdater.updateVersions()







