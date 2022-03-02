from schema import process_schema
from jsonmerge import merge

def parameter(name, schema):
    schema_spec = process_schema(schema)
    return merge({'path_name': name}, schema_spec)

def header(name, schema):
    return {}

def query(name, schema):
    schema_spec = process_schema(schema)
    return merge({'path_name': name}, schema_spec)
