# README

1. Go to app/
2. Build the container
````bash
docker build -t myapp .
````
3. Find the container id
```bash
docker ps
```
4. Launch it
````bash
docker run -p 8000:8000 <id container>
````

Merci de m'avoir lu