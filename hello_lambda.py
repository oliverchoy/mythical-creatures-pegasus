import requests

def lambda_handler(json_input, context):
    print(json_input)
    print(context)
    print("Hello Pegasus")

if __name__ == '__main__':
    lambda_handler({}, None)
