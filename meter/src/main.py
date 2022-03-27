import meter
from shared import connection_handler


def main():
    connection, channel, queue = connection_handler.setup_rabbitmq()
    meter.send_meter_values(channel, queue)
    print("All messages sent")
    connection.close()


if __name__ == "__main__":
    main()
