from schema_body import process_schema_body

class Body:
    def __init__(self, spec):
        self._which_func = {
            "application/json": self.process_json,
        }
        """
        Crear funcionar para cada tipo del body
        Sobre todo, para estas
        "application/x-www-form-urlencoded": self.process_form_urlencoded,
        "multipart/form-data": self.process_form_data,
        "application/xml": self.process_xml
        """
        self._body_header = {}
        self._body_body = {}
        self._spec = spec

    def process_body(self, body):
        self._body_header = list(body.keys())[0]
        self._which_func[self._body_header](body[self._body_header]["schema"])

    def process_json(self, schema):
        spec_schema = process_schema_body(schema["properties"], self._spec)
        self._body_body = spec_schema