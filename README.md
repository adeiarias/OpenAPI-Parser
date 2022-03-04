# OpenAPI-Parser

## USAGE
<pre>
[*] USAGE: python openapi_parser.py spec_file spec_format
** spec_format ** MUST BE EITHER JSON OR YAML

For example:
If the openapi file is "openapi3.yaml"
</pre>
```
python openapi_parser.py openapi3.yaml yaml
```
The second argument to specify file format is not key sensitive, so it could also be written as YAML or Yaml
<pre>
Example with a YAML openapi file

URL: http://localhost:5000/
-------------------------------------------------------
Path: /createdb
Method: get
URI parameters: []
-------------------------------------------------------
Path: /
Method: get
URI parameters: []
-------------------------------------------------------
Path: /users/v1
Method: get
URI parameters: []
-------------------------------------------------------
Path: /users/v1/_debug
Method: get
URI parameters: []
-------------------------------------------------------
Path: /users/v1/register
Method: post
URI parameters: []
Body: {'username': {'type': 'string'}, 'password': {'type': 'string'}, 'email': {'type': 'string'}}
-------------------------------------------------------
Path: /users/v1/login
Method: post
URI parameters: []
Body: {'username': {'type': 'string'}, 'password': {'type': 'string'}}
-------------------------------------------------------
Path: /users/v1/{username}
Method: get
URI parameters: [{'path_name': 'username', 'type': 'string'}]
-------------------------------------------------------
Path: /users/v1/{username}
Method: delete
URI parameters: [{'path_name': 'username', 'type': 'string'}]
-------------------------------------------------------
Path: /users/v1/{username}/email
Method: put
URI parameters: [{'path_name': 'username', 'type': 'string'}]
Body: {'email': {'type': 'string'}}
-------------------------------------------------------
Path: /users/v1/{username}/password
Method: put
URI parameters: [{'path_name': 'username', 'type': 'string'}]
Body: {'password': {'type': 'string'}}
-------------------------------------------------------
Path: /books/v1
Method: get
URI parameters: []
-------------------------------------------------------
Path: /books/v1
Method: post
URI parameters: []
Body: {'book_title': {'type': 'string'}, 'secret': {'type': 'string'}}
-------------------------------------------------------
Path: /books/v1/{book}
Method: get
URI parameters: [{'path_name': 'book', 'type': 'string'}]
-------------------------------------------------------
</pre>

