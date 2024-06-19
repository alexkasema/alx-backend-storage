# Redis basic
* Open source in-memory data structure store which can be used as a database and/or a cache and message broker.
* NoSQL key/value store
* Supports multiple data structures
* Built in Replication (master-slave)
Redis has a client-server architecture and uses a request-response model. This means that you (the client) connect to a Redis server through TCP connection, on port 6379 by default. You request some action (like some form of reading, writing, getting, setting, or updating), and the server serves you back a response.

There can be many clients talking to the same server, which is really what Redis or any client-server application is all about. Each client does a (typically blocking) read on a socket waiting for the server response.

The cli in redis-cli stands for command line interface, and the server in redis-server is for, well, running a server. In the same way that you would run python at the command line, you can run redis-cli to jump into an interactive REPL (Read Eval Print Loop) where you can run client commands directly from the shell.

First, however, you’ll need to launch redis-server so that you have a running Redis server to talk to. A common way to do this in development is to start a server at localhost (IPv4 address 127.0.0.1), which is the default unless you tell Redis otherwise. You can also pass redis-server the name of your configuration file, which is akin to specifying all of its key-value pairs as command-line arguments
## exercise.py
Writing strings to Redis
Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.
