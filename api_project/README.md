# API Authentication and Permissions

This API uses token-based authentication. To access protected endpoints, follow these steps:

1. Obtain a token by sending a POST request to `/api-token-auth/` with your username and password.
2. Include the token in the Authorization header of your requests:
   `Authorization: Token your_token_here`

All book-related endpoints require authentication. Unauthenticated requests will receive a 401 Unauthorized response.
