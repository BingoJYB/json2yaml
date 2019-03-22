# json2yaml

Transformer for JSON Schema files into YAML format.

## Getting Started

These instructions will guide you how to use this transformer to convert the JSON Schema to YAML format.

### Prerequisites

One external Python module called PyYAML needs to be installed which is under MIT license. Simple install:

```sh
pip install pyyaml
```

## Running the transformer

The transformer accepts two arguments. One is the file name of the input JSON Schema file and the other is the file name of the output YAML file.

```sh
generator.py [JSON Schema file] [YAML file]
```

One example is:

```
generator.py rulesets.json rulesets.yaml
```