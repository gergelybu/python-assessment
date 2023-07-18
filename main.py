import json

# Asking for the configuration file from the user
json_file_path = input("Enter the path to the configuration file: ")

with open(json_file_path) as json_file:
    json_data = json.load(json_file)