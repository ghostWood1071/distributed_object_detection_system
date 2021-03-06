import datetime
from flask import Flask, Response
from kafka import KafkaConsumer
from detect import detector

# Fire up the Kafka Consumer
topic = "distributed-video1"

consumer = KafkaConsumer(
    topic, 
    bootstrap_servers=['10.0.2.196:9092'])

object_detect = detector()

# Set the consumer in a Flask App
app = Flask(__name__)

@app.route('/video', methods=['GET'])
def video():
    return Response(
        get_video_stream(), 
        mimetype='multipart/x-mixed-replace; boundary=frame')

def get_video_stream():
    """
    Here is where we recieve streamed images from the Kafka Server and convert 
    them to a Flask-readable format.
    """
    for msg in consumer:
        frame = object_detect.to_matrix(msg.value)
        result = object_detect.detect(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + result + b'\r\n\r\n')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)