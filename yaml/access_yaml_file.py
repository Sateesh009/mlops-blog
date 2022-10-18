# Read YAML file from a python script.

import pprint

with open('sample_yaml_file.yaml') as conf_file:
# All parameters defined in YAML file are stored into a dictionary called config
    config = yaml.safe_load(conf_file)

pprint.pprint(config)
