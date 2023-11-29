import requests

def parse_swagger(swagger_url):
    response = requests.get(swagger_url)
    swagger_data = response.json()

    paths = swagger_data.get("paths", {})

    print("Endpoints:")
    for path in paths:
        print(path)

if __name__ == "__main__":
    swagger_url = "https://petstore.swagger.io/v2/swagger.json"
    parse_swagger(swagger_url)
