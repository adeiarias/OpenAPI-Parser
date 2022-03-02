def process_schema_body(input_schema, spec):
    return_json = {}
    for key in input_schema:
        return_json[key] = {}
        for value in input_schema[key]:
            if(value == "$ref"):
                try:
                    return_json[key] = get_ref_info(input_schema[key][value], key, spec)
                except:
                    pass
            else:
                try:
                    return_json[key][value] = schema_func[value](input_schema[key])
                except:
                    pass
    return return_json

def get_ref_info(ref, key, spec):
    ref_info = ref.split("/")[1:]
    info = {}
    for elem in ref_info:
        try:
            info = info[elem]
        except:
            info = spec["components"]

    json_to_return = {}
    for elem in info:
        json_to_return[elem] = info[elem]
        
    return json_to_return

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
    json = {}
    for key in schema["properties"]:
        json[key] = {}
        for value in schema["properties"][key]:
            try:
                json[key][value] = schema_func[value](schema["properties"][key])
            except:
                pass
    return json

schema_func = {
    "type": type_funct,
    "enum": enum_funct,
    "format": format_funct,
    "minimum": minimum_funct,
    "maximum": maximum_funct,
    "properties": json_schema_funct,
}