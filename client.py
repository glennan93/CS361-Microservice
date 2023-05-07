import time
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
time.sleep(1)
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Send request and wait for response

print("Sending request…")
socket.send_string('2')
time.sleep(1)

    #  Get the reply.
message = socket.recv()
message = message.decode('utf-8')
print(f"Received reply [ {message} ]" )