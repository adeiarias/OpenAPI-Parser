import yaml, sys, json, re
from path import Path

spec = ""
openapi_object = ["openapi", "info", "servers", "paths", "components", "security", "tags", "externalDocs"]
url = ""

def load_spec(spec_path, spec_type): # la especificación puede ser tanto un yaml como un json
    global spec

    if spec_type.lower() == "yaml":
        try:
            spec = yaml.safe_load(open(spec_path))
        except yaml.YAMLError as exc:
            print(exc)    

    elif spec_type.lower() == "json":
        try:
            spec = json.load(open(spec_path, "r"))
        except json.JSONDecodeError as exc:
            print(exc)

    else:
        raise Exception("Invalid spec type")

def verify_openapi_object():   
    for key in spec.keys():
        if key not in openapi_object:
            raise Exception("Invalid '" + str(key) + "' openapi object")    

    for key in openapi_object[0:4]:
        if key not in spec:
            raise Exception("Missing '" + str(key) + "' in openapi specification")    

def url_parser():
    # Conseguir la url base de la especificación. Si hubiera parámetros en la url, se sustituirán por los valores por defecto de los parámetros
    global url
    server = spec["servers"][0]
    if "url" not in server:
        raise Exception("Server URL not found")
    else:
        url = server["url"]
        if len(re.findall('[{]*[A-Za-z]*[}]', url)) > 0:
            params = re.findall('[{]*[A-Za-z]*[}]', url)
            for param in params:
                url = url.replace(param, server["variables"][param[1:-1]]["default"])

def process_paths():
    paths = spec["paths"]
    processed_path_list = []
    for path in paths:
        if path[0] != "/":
            pass # Se pasa un ref, luego lo programo
        else:
            for method in spec["paths"][path]:
                processed_path = Path(spec)
                processed_path._path = path
                processed_path._method = method
                if "responses" not in spec["paths"][path][method]:
                    raise Exception("No responses found in path " + str(path) + " method " + str(method))
                if "parameters" in spec["paths"][path][method]:

                    processed_path.parameters(spec["paths"][path][method]["parameters"])
                if "requestBody" in spec["paths"][path][method]:
                    if(list(spec["paths"][path][method]["requestBody"].keys())[0] == "$ref"):
                        try: # Mirar en los components de la especificación
                            processed_path.body(get_body_from_ref(spec["paths"][path][method]["requestBody"]["$ref"].split("/")[1:])) # Para quitar los '/' y la '#' del inicio
                        except:
                            raise Exception("Invalid requestBody reference")
                    else:
                        processed_path.body(spec["paths"][path][method]["requestBody"]["content"])
                processed_path_list.append(processed_path)
    return processed_path_list

def get_body_from_ref(ref):
    body = {}
    for elem in ref:
        try:
            body = body[elem]
        except:
            body = spec["components"]
    return body["content"]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python openapi_parser.py <spec_path> <spec_type>")
        exit(1)
    load_spec(sys.argv[1], sys.argv[2])
    verify_openapi_object()
    url_parser()
    list = process_paths()
    output_results = open("output.txt", "w")
    output_results.write("URL: " + str(url) + "\n")
    output_results.write("-------------------------------------------------------\n")
    for elem in list:
        path = elem._path
        method = elem._method
        params = elem._parames
        body = elem._body
        responses = elem._responses
        
        try:
            output_results.write("Path: " + path + "\n")
            output_results.write("Method: " + method + "\n")
            output_results.write("URI parameters: " + str(params) + "\n")
            output_results.write("Body: " + str(body._body_body) + "\n")
        except:
            pass
        output_results.write("-------------------------------------------------------\n")
    # La especificación se ha cargado correctamente y se ha verificado que el objeto openapi es correcto

