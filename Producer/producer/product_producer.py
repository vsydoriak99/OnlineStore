import json

from producer.base_producer import BaseProducer


class ProductProducer(BaseProducer):

    def __init__(self, args):
        super().__init__(args)

    def send_request(self, key: str, value: json):
        try:
            self.producer.produce(topic=self.topic, key=key, value=value)
        except Exception as e:
            print(f'Ex {e}')
        else:
            print(f"Successfully product request barcode {key}, value {value}")

    def send_requests(self, products: list):
        for product in products:
            self.send_request(key=product.barcode, value=product.to_json())
        self.producer.flush()
