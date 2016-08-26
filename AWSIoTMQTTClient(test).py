from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("Device34")
myMQTTClient.configureEndpoint("a1trumz0n7avwt.iot.us-west-2.amazonaws.com",8883)
myMQTTClient.configureCredentials("data/root-CA.txt", "data/device34.key", "data/device34.txt")
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)
