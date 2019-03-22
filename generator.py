import json
import sys
import yaml


def read_json_schema(input_file_name):
    with open(input_file_name) as input_file:
        json_schema = json.load(input_file)

    return json_schema


def generate_yaml(json_schema):
    generated_yaml = yaml.dump(json_schema, default_flow_style=False)

    return generated_yaml


def validate_yaml(yaml_file):
    try:
        yaml.safe_load(yaml_file)
        return yaml_file
    except:
        sys.exit('Failed to validate file.')


if __name__ == '__main__':
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    json_schema = read_json_schema(input_file_name)
    yaml_file = generate_yaml(json_schema)
    valid_yaml_file = validate_yaml(yaml_file)
    output_file = open(sys.argv[2], "w")
    output_file.write(valid_yaml_file)
    output_file.close()
    print("Finished!")
