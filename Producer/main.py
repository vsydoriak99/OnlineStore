
# Press the green button in the gutter to run the script.
from start_producer.producer_factory import ProducerFactory

if __name__ == '__main__':
    producer_factory = ProducerFactory('product')
    producer_factory.sending()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
