import sys
import time
import cv2
from kafka import KafkaProducer

def publish_camera(topic, video):
    producer = KafkaProducer(bootstrap_servers=['10.0.2.196:9092','10.0.2.197:9093'])
    camera = cv2.VideoCapture(video)
    try:
        while(True):
            success, frame = camera.read()
            producer.send(topic, frame.tobytes())
            time.sleep(0.2)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        topic_name = sys.argv[1]
        video_path = sys.argv[2]
        publish_camera(topic_name, video_path)
    else:
        print("dont have any topic or video")
