# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
from socket import socket

from confluent_kafka import Producer

from entities.user import User
from producer.user_producer import UserProducer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def method_name():
    users = [User.generateRandomUser() for i in range(10)]
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema_registry', default='http://localhost:8081')
    parser.add_argument('--bootstrap_servers', default='localhost:9092')
    parser.add_argument('--topic', default='camp-user')
    parser.add_argument('--schema_file', default='schema_CreateUserRequest.avsc')
    list_arg = parser.parse_args()
    user_producer = UserProducer(list_arg)
    user_producer.send_requests(users)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    method_name()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
