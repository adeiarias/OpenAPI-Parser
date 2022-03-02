# OpenAPI-Parser

## USAGE
<pre>
   [*] USAGE: python openapi_parser.py spec_file spec_format
   ** spec_format ** MUST BE EITHER JSON OR YAML
</pre>
<pre>
Example with Petstore openapi file

URL: http://petstore.swagger.io/v1
-------------------------------------------------------
Path: /pets
Method: get
URI parameters: []
-------------------------------------------------------
Path: /pets
Method: post
URI parameters: []
-------------------------------------------------------
Path: /pets/{petId}
Method: get
URI parameters: [{'path_name': 'petId', 'type': 'string'}]
-------------------------------------------------------
</pre>

