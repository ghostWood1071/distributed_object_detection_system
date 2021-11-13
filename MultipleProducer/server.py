from flask import Flask, Response
from streamer import Streamer;
import sys

class Server:
    def __init__(self,app,topic, port=5000) -> None:
        self.streamer = Streamer(topic)
        self.port = port
        self.app = app
    def run(self):
        @self.app.route('/video', methods=['GET'])
        def video():
            return Response(
                self.streamer.get_data(), 
                mimetype='multipart/x-mixed-replace; boundary=frame')
        self.app.run(host='0.0.0.0', debug=True, port=self.port)

if __name__ == "__main__":
    if(len(sys.argv)):
        topic = sys.argv[1]
        app_port = int(sys.argv[2])
        server = Server(Flask(topic), topic, app_port)
        server.run()
    else:
        print("no parameters have provided")