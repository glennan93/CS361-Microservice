# CS361 Pokemon TCG Microservice

## Description
This microservice generates the name of a random Pokemon card when requested. 

## Requests and Responses
Requests and responses are sent using ZeroMQ. 

## Setup

### API Key

An API key is needed to use the PokemonTCG API.  To register for an API key, one must create an account at https://dev.pokemontcg.io/.

### Server

To run the server, download server.py into a parent directory and run the file in the terminal.

### Client

To run the client, download client.py into the same parent directory and run the file in the terminal. 

## How to request data from the microservice.

Requests to the server are made by sending strings.  The server listens for the string, '2'.  If the server receives that request, it will generate a random Pokemon card name and send  that name back as a string to the client.

An example call from client to server using ZeroMQ might look like this:

socket.send_string("2")

## How to receive data from the microservice.  

When the proper request is made to the server, it will request a card set from the PokemonTCG API and randomly select a card name from that set.
Once the name of the card is generated, the microservice will send that name as a string back over the ZeroMQ socket to the client.  

## UML Sequence Diagram
![Screenshot from 2023-05-07 16-42-35](https://user-images.githubusercontent.com/97012693/236703961-3121da99-9358-4085-8ec6-80220413f2cd.png)


