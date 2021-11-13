import datetime
import sys
from flask import Flask, Response
from kafka import KafkaConsumer
from detect import detector

# Fire up the Kafka Consumer
topic = ""
app_port = 5000
consumer = KafkaConsumer(
    topic, 
    bootstrap_servers=['10.0.2.196:9092', '10.0.2.197:9093'])

object_detect = detector()

app = Flask(__name__)

@app.route('/video', methods=['GET'])
def video():
    return Response(
        get_video_stream(), 
        mimetype='multipart/x-mixed-replace; boundary=frame')

def get_video_stream():
    for msg in consumer:
        frame = object_detect.to_matrix(msg.value)
        result = object_detect.detect(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + result + b'\r\n\r\n')

if __name__ == "__main__":
    if(len(sys.argv)):
        topic = sys.argv[1]
        app_port = int(sys.argv[2])
        app.run(host='0.0.0.0', debug=True, port=app_port)
    else:
        print("no parameters have provided")