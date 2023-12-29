# Docker setup note

A production Dockerfile is intentionally not included yet. Start with a slim Python image, install requirements, collect static files only if the project serves them, and run the app behind a real WSGI server.

## Future Docker thought

Docker should wait until the runtime shape is clearer. A premature Dockerfile would probably need churn later.
