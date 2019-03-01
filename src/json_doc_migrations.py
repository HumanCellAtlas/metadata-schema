from argparse import ArgumentParser
import json
from collections import defaultdict
from itertools import chain
import copy

class Migrator:

    def add_property(self, json_doc, migration):
        new_prop = migration["property"]
        if "default_value" in migration:
            value = migration["default_value"]

            for part in reversed(new_prop.split('.')):
                value = {part: value}

            new_json_doc = copy.deepcopy(json_doc)
            new_json_doc = self._mergeDict(new_json_doc, value)
        return self._update_schema_version(new_json_doc, migration["effective_from"])

    def remove_property(self, json_doc, migration):
        source_prop = migration["property"].split(".")

        new_json_doc = copy.deepcopy(json_doc)
        new_json_doc = self._removeSourceProp(new_json_doc, source_prop)

        return self._update_schema_version(new_json_doc, migration["effective_from"])

    def move_property_in_schema(self, json_doc, migration):
        source_prop = migration["property"].split(".")
        new_prop = migration["replaced_by"]

        value = json_doc
        for key in source_prop:
            value = value[key]
        for part in reversed(new_prop.split('.')):
            value = {part: value}

        new_json_doc = copy.deepcopy(json_doc)
        new_json_doc = self._mergeDict(new_json_doc, value)
        new_json_doc = self._removeSourceProp(new_json_doc, source_prop)

        return self._update_schema_version(new_json_doc, migration["effective_from"])

    def move_property_across_schemas(self, json_doc, target_doc, migration):
        source_prop = migration["property"].split(".")
        new_prop = migration["replaced_by"]

        value = json_doc
        for key in source_prop:
            value = value[key]
        for part in reversed(new_prop.split('.')):
            value = {part: value}

        if new_prop.split('.')[0] not in target_doc.keys():
            new_target_doc = self._mergeDict(target_doc, value)
        new_json_doc = self._removeSourceProp(json_doc, source_prop)

        return self._update_schema_version(new_json_doc, migration["effective_from_source"]), self._update_schema_version(new_target_doc, migration["effective_from_target"])

    def _update_schema_version(self, json_doc, new_version):
        schema_uri = json_doc["describedBy"]
        current_version = json_doc["schema_version"]

        new_uri = schema_uri.replace(current_version, new_version)

        json_doc["describedBy"] = new_uri
        json_doc["schema_version"] = new_version
        return  json_doc

    def _mergeDict(self, dict1, dict2):
        dict3 = defaultdict(list)
        for k, v in chain(dict1.items(), dict2.items()):
            if k in dict3:
                if isinstance(v, dict):
                    dict3[k].update(self._mergeDict(dict3[k], v))
                elif isinstance(v, list) and isinstance(dict3[k], list) and len(v) == len(dict3[k]):
                    for index, e in enumerate(v):
                        dict3[k][index].update(self._mergeDict(dict3[k][index], e))
                else:
                    dict3[k].update(v)
            else:
                dict3[k] = v
        return dict3

    def _removeSourceProp(self, json_dict, prop):
        for k in json_dict.keys():
            if k in prop:
                if isinstance(json_dict[k], dict):
                    self._removeSourceProp(json_dict[k], prop)
                elif isinstance(json_dict[k], list):
                    for item in json_dict[k]:
                        if isinstance(item, dict):
                            self._removeSourceProp(item, prop)
                        elif k == prop[-1]:
                            del json_dict[k]
                            break
                elif k == prop[-1]:
                    del json_dict[k]
                    break
        return json_dict


def _open_file(filename):
    f = open(filename, 'r')
    return json.loads(f.read())

def _save_json(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)




if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-f", "--f", dest="files", action="append",
                      help="JSON documents to migrate")
    parser.add_argument("-m", "--m", dest="migration",
                      help="Migration document")

    args = parser.parse_args()

    docs = []

    if args.files:
        for file in args.files:
            docs.append(_open_file(file))
    else:
        print("You have to provide a JSON document to migrate")
        exit(2)

    if args.migration:
        migration = _open_file(args.migration)
    else:
        print("You have to provide a migration strategy document")
        exit(2)

    for doc in docs:
        for m in migration["migrations"]:
            if m["source_schema"] in doc["describedBy"]:
                if "effective_from" in m and int(m["effective_from"].split(".")[0]) >= int(doc["schema_version"].split(".")[0]):
                    if "replaced_by" not in m and "default_value" in m:
                        new_doc = Migrator().add_property(doc, m)
                        docs[docs.index(doc)] = new_doc
                        doc = new_doc
                    elif "replaced_by" not in m and "default_value" not in m:
                        new_doc = Migrator().remove_property(doc, m)
                        docs[docs.index(doc)] = new_doc
                        doc = new_doc
                    elif m["source_schema"] == m["target_schema"]:
                        new_doc = Migrator().move_property_in_schema(doc, m)
                        docs[docs.index(doc)] = new_doc
                        doc = new_doc
                elif "effective_from_source" in m and int(m["effective_from_source"].split(".")[0]) >= int(doc["schema_version"].split(".")[0]):
                    for target_doc in docs:
                        if m["target_schema"] in target_doc["describedBy"] and int(m["effective_from_target"].split(".")[0]) >= int(doc["schema_version"].split(".")[0]):
                            new_docs = Migrator().move_property_across_schemas(doc, target_doc, m)
                            docs[docs.index(doc)] = new_docs[0]
                            docs[docs.index(target_doc)] = new_docs[1]
                            doc = new_docs[0]

    counter = 0
    for doc in docs:
        _save_json("updated_file_" + str(counter) + ".json", doc)
        counter += 1



