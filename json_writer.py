import json
import os

class JsonWriter(object):

  def write(self, file_path, new_data_dict={}):
    current_data_list = []

    # If we have a JSON named by the source, read it in
    if os.path.exists(file_path):
      with open(file_path, "r") as jsonFile:
        current_data_list = json.load(jsonFile)

    # If this article is not already in the json (check this by URL), add it to the list
    if new_data_dict["url"] not in [current_data_dict["url"] for current_data_dict in current_data_list]:
      current_data_list.append(new_data_dict)

    # Write to a json file with the source as its name
    with open(file_path, "w") as jsonFile:
      json.dump(current_data_list, jsonFile)

