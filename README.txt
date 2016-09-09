A toy app/service, consumer, and service broker for playing with cloud foundry.


Echo app endpoints:

/
Returs "Hello, World!"

/goodbye
Returs "Goodbye!"

/echo
Echoes back the value sent of the "data" request argument.
An app that consumes my toy echo application as a service.
A service broker for my toy echo application.


Echo consumer uses the Echo app to handle the /echo endpoint.


The echo service broker is a very crude, minimal service broker for
the echo app's /echo endpoint.
