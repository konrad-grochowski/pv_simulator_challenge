import pika
import time
import os


def get_connection(host, credentials):
    """
    Function for getting rabbitMQ connection
    """
    for attempt_number in range(1, 6):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host, credentials=credentials))
            return connection
        except (pika.exceptions.ConnectionClosed, pika.exceptions.AMQPConnectionError) as e:
            print(e)
            print(
                f"Attempt no. {attempt_number}. Connection could not be achieved. Retrying...")
            # avoid rapid reconnection on longer RMQ server outage
            time.sleep(5)


def setup_rabbitmq():
    host = os.environ['RABBITMQ_HOST']
    queue = os.environ['RABBITMQ_QUEUE']
    user = os.environ['RABBITMQ_DEFAULT_USER']
    password = os.environ['RABBITMQ_DEFAULT_PASS']

    credentials = pika.PlainCredentials(user, password)
    connection = get_connection(host, credentials)
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    return connection, channel, queue
