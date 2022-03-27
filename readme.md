# PV Simulator challenge
This repository contains simulations of PV power values and household electrical energy consumption.
These two simulations take place on separate docker containers and communicate using RabbitMQ broker, in producer-consumer fashion.
The consumption simulator generates the power consumption values accross time, 
then sends them through the RabbitMQ broker system to PV simulator acting as a consumer,
which eventually saves the received value and simulated PV power value to the .csv file.
# Execution
To run the simulations, common.env file needs to be created at the root of this catalogue system.
It has to contain following values:
1. RABBITMQ_QUEUE, the name of the queue the producer and consumer will run on;
2. RABBITMQ_DEFAULT_USER, default user for RabbitMQ 
3. RABBITMQ_DEFAULT_PASS, default password for RabbitMQ
4. METER_SENDING_SPEED, a coefficient by which the simulation speed will be multiplied. Value equal to 1 will result in matching simulation time with real time, and the simulation will last 24 hours. Value equal to 1000 will make the simulation last approximately 1.5 minutes.

After filling the common.env file, run:
```console
docker-compose up --build
```
This will trigger building and executing the simulation. The log file will be created in /logs catalogue at the root of the repository.
It will contain the following columns:
1. Timestamp from midnight, in seconds
2. Consumption value from the "meter" component
3. Simulated PV power value
4. Sum of consumption and PV power value.