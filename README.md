# IoT-connect-with-MQTT
I created an Internet of Things (IoT) server. This server utilized several technologies, all running within Docker containers. Specifically, it used Mosquitto MQTT for message brokering, InfluxDB for time-series data storage, Node-RED for flow-based programming, and Grafana for data visualization.
I created a flow in Node-RED that subscribes to a specific MQTT topic, processes the incoming messages, and then republishes the processed messages to another topic.

Steps : 

1)MQTT Input Node : Subscribes to the topic /training/device/Eduard-Radu.This node receives messages published to this topic.

2)Debug Node 1 : Connected to the MQTT Input node to display the received messages in the debug panel for monitoring purposes.

3)Function Node : Processes the incoming message.This node can be used to perform any transformation or computation on the message

4)Debug Node 2 : Connected to the Function node to display the processed messages in the debug panel, allowing verification of the changes made.

5)MQTT Output Node : Publishes the processed messages to the topic /training/device/Eduard-Radu/processed.This allows other subscribers to receive the modified messages.

To simulate the transmission of sensor data to Node-Red, I used the script simulation.py . This script employs the paho.mqtt.client library to publish randomly generated sensor data to a specified MQTT topic.

Explanation :
- I used the MQTT broker "mqtt.beia-telemetrie.ro."I used the standard MQTT port, 1883.The MQTT topic /training/device/Eduard-Radu/ is specified for publishing the sensor data.
- The generate_sensor_data function creates random values for temperature (15.0 to 30.0°C), pressure (900.0 to 1050.0 hPa), humidity (30.0 to 70.0%), and gas (0.0 to 100.0 units). These values simulate realistic sensor readings.
- I created an MQTT client and connected it to the broker using the connect method.
- The script enters a loop where it continuously generates sensor data and publishes it to the specified MQTT topic every 5 seconds. The print statement outputs the sent data to the console for verification.
- The loop can be interrupted with a keyboard interrupt (Ctrl+C), which stops the loop and disconnects the MQTT client gracefully.

I used InfluxDB to store sensor data received via Node-Red. By executing a command in a Docker container running InfluxDB, I connected to the InfluxDB shell (version 1.8.10). I then selected the database named "sensor_data" and displayed its measurements. Finally, I executed a query to retrieve all records from the "sensor_data" measurement, which includes fields for gas, humidity, pressure, and temperature along with their respective timestamps. The data shows various readings, illustrating how I monitored and recorded environmental conditions over time.

Using Grafana, I developed an interactive and dynamic dashboard for visualizing real-time IoT data stored in InfluxDB. The setup allowed for monitoring environmental conditions such as temperature, pressure, humidity, and gas levels. The dashboards included:

- Time-Series Graphs: Displaying trends over time for metrics like temperature.
- Gauges: Providing a quick overview of real-time readings.
- Alerting System: Configured to notify users when specific thresholds (e.g., temperature above 28°C) were exceeded. Notifications were sent via email and Telegram for prompt intervention.
- This implementation made it easier to analyze, monitor, and act upon IoT data, enhancing the overall system's functionality and responsiveness. 

Moreover, I needed to create a bot on Telegram. This can be done by talking to the BotFather, which is a bot that helps you create and manage your Telegram bots. Once created, I received a unique token that allows me to authenticate and interact with the Telegram API. I required my Telegram user ID and utilized IDBot to obtain it. I developed this bot to provide real-time environmental data upon request. By sending the command /data, the bot prompts for a selection, allowing the user to choose between different types of data such as temperature, humidity, air pressure, and air quality. 

Sub-Flow:

/data: This node receives a /data command from the user on Telegram.

function 1: This function processes the received command and prepares the response.

Telegram sender: Sends a message through Telegram to the user, asking for a selection of the desired data (temperature, humidity, air pressure, air quality).

Another Sub-Flow:

callback_query: This node receives a selection from the user based on the response sent by the Telegram sender.

function 2: This function processes the user's selection and prepares the query to fetch the specific data.

[v1.x] 172.31.179.115:8086/sensor_data: The specific data is requested from the sensor data endpoint.

function 3: The function processes the received data and prepares it to be sent back to the user on Telegram.

Telegram sender: Sends the requested data to the user on Telegram.

debug 4 and debug 3: The debug nodes display the information to verify the correctness of the processed and sent data.

By integrating a Telegram ChatBot into my project, I can leverage the power of real-time messaging to enhance monitoring and control. The bot can can interact with me to provide data on demand. This addition makes my IoT setup more robust, user-friendly, and responsive.
