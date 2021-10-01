import argparse
import random
from abc import ABC, abstractmethod
import time

from entities.product import Product
from entities.user import User
from producer.product_producer import ProductProducer
from producer.user_producer import UserProducer


class ProducerFactory:

    def __init__(self, type_object):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--schema_registry', default='http://localhost:8081')
        self.parser.add_argument('--bootstrap_servers', default='localhost:9092')
        self.parser.add_argument('--topic', default=type_object)
        self.parser.add_argument('--schema_file', default=f'schema_{type_object}.avsc')
        self.parser.parse_args()
        if type_object == 'user':
            self.producer = UserProducer(self.parser.parse_args())
            self.obj = User
        elif type_object == 'product':
            self.producer = ProductProducer(self.parser.parse_args())
            self.obj = Product
        else:
            raise Exception

    def sending(self, max_bach_size=100, time_sleep=10):
        while True:
            rand_int = random.randint(a=1, b=max_bach_size+1)
            print(f'Batch size = {rand_int}')
            object_list = [self.obj.generateRandom() for _ in range(rand_int)]
            self.producer.send_requests(object_list)
            time.sleep(time_sleep)
