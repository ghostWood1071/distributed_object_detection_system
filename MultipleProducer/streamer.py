import sys
from flask import Flask, Response
from kafka import KafkaConsumer
from detect import detector

class Streamer:
    def __init__(self, topic):
        self.topic = topic
        self.consumer = KafkaConsumer(topic,bootstrap_servers=['10.0.2.196:9092', '10.0.2.197:9093'])
        self.detector = detector()
    def get_data(self):
        for msg in self.consumer:
            frame = self.detector.to_matrix(msg.value)
            result = self.detector.detect(frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpg\r\n\r\n' + result + b'\r\n\r\n')

