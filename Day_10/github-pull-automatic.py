import requests

response = requests.get("https://api.github.com/repos/rama722/python_devops/pulls")

# print(type(response))

# print(response.json())   # when you use json its automatically create dictionary format.

# print(response.status_code)

complete_detail = response.json()

for element in range(len(complete_detail)):

    print(complete_detail[element]["user"]["login"])