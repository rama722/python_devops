ec2_instance = [
    {
        "name": "ec2_instnace01",
        "type": "t2.micro"
    },
    {
        "name": "ec2_instnace02",
        "type": "t2.medium"
    },
    {
        "name": "ec2_instnace03",
        "type": "t2.large"
    }
]

print(ec2_instance)

print(ec2_instance[2]["type"])  # if you want specfice one you can use 