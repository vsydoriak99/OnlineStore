import json

from producer.base_producer import BaseProducer


class UserProducer(BaseProducer):

    def __init__(self, args):
        super().__init__(args)

    def send_request(self, key: str, value: json):
        try:
            self.producer.produce(topic=self.topic, key=key, value=value)
        except Exception as e:
            print(f'Ex {e}')
        else:
            print(f"Successfully user request {key}, {value}")
            
    def send_requests(self, users: list):
        for user in users:
            self.send_request(key=user.email, value=user.to_json())
        self.producer.flush()
