Command-Line Arguments
Python provides the sys and argparse modules to handle command-line arguments.

Using sys.argv
sys.argv is a list where:
sys.argv[0] is the name of the script.
sys.argv[1:] are the command-line arguments passed to the script.
Example:

python
Copy code
import sys

# Print all command-line arguments
print("Arguments:", sys.argv)

# Access specific arguments
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])
else:
    print("No arguments provided!")
Using argparse (Recommended)
argparse is more robust and allows you to define expected arguments with types, defaults, and help messages.
Example:

python
Copy code
import argparse

# Create parser
parser = argparse.ArgumentParser(description="Process some command-line arguments.")

# Define arguments
parser.add_argument('--name', type=str, help='Your name', required=True)
parser.add_argument('--age', type=int, help='Your age', default=18)

# Parse arguments
args = parser.parse_args()

print(f"Name: {args.name}")
print(f"Age: {args.age}")
Run:

bash
Copy code
python script.py --name Alice --age 25
Environment Variables
You can use the os module to access environment variables.

Reading Environment Variables
Example:

python
Copy code
import os

# Access environment variables
db_host = os.getenv('DB_HOST', 'localhost')  # Provide a default value if the variable doesn't exist
db_user = os.environ.get('DB_USER', 'root')

print("Database Host:", db_host)
print("Database User:", db_user)
Setting Environment Variables
You can set environment variables in Python for the current process:

python
Copy code
os.environ['DB_PASSWORD'] = 'mysecurepassword'
print("Database Password:", os.environ['DB_PASSWORD'])
Combining Command-Line Args & Environment Vars
You can use both to provide flexibility:

Use environment variables as defaults.
Allow overriding them with command-line arguments.
Example:

python
Copy code
import os
import argparse

# Environment variables
db_host = os.getenv('DB_HOST', 'localhost')

# Command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--db-host', type=str, help='Database host', default=db_host)
args = parser.parse_args()

print(f"Database Host: {args.db_host}")
Run:

bash
Copy code
DB_HOST=127.0.0.1 python script.py --db-host 192.168.1.1
Output:

yaml
Copy code
Database Host: 192.168.1.1
