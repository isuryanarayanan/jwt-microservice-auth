# jwt-microservice-auth

Microservice authorization using multiple JWT tokens (wallmart oauth2)

## Authentication server

#### Login route

```
https://localhost:port/tokens/login/
```

This is the only route exposed to the client from the authentication server.
Provides a rest api when a post request is made with suffiecient user credentials will return a set of access tokens.
The initial set of tokens will be for the authentication server itself which will allow refreshing and generation of the jwt tokens.
