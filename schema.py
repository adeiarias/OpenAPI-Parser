def process_schema(input_schema):
    return_json = {}
    for key in input_schema:
        try:
            return_json[key] = schema[key](input_schema)
        except:
            pass
    return return_json

def type_funct(schema):
    return schema["type"]

def enum_funct(schema):
    return schema["enum"]

def format_funct(schema):
    if "byte" in schema["format"]:
        return "base64"
    elif "binary" in schema["format"]:
        return "octal"
    elif "date" in schema["format"]:
        return "date"
    elif "date-time" in schema["format"]:
        return "date-time"
    else: # Como hay un try except, va a pasar al siguiente
        raise Exception("Format not supported")

def minimum_funct(schema):
    return schema["minimum"]

def maximum_funct(schema):
    return schema["maximum"]

def json_schema_funct(schema):
    pass

schema = {
    "type": type_funct,
    "enum": enum_funct,
    "format": format_funct,
    "minimum": minimum_funct,
    "maximum": maximum_funct,

}