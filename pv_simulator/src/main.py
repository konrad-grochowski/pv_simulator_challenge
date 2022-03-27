from datetime import datetime
from callback_handler import create_callback
from shared import connection_handler

def main():
    """
    Function opens up the RabbitMQ connection and sets the callback for consuming.
    Handling the messages is delegated to the "callback_handler" package.
    """
    connection, channel, queue = connection_handler.setup_rabbitmq()
    logs_timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    channel.basic_consume(queue=queue,
                          auto_ack=True,
                          on_message_callback=create_callback(logs_timestamp)
                          )
    channel.start_consuming()


if __name__ == "__main__":
    main()
