# Running the training notebook

- go to the trainig folder
```
cd training
```

- build and run the docker container
```
docker-compose up --build
```

# Running the server
- go to the server folder
```
cd server
```

- build and run the docker container
```
docker-compose up --build
```

Server should be up on `http://172.18.0.3:5000/`.
You can make POST request to `/v1/categorize`. More instructions
available on [server README](https://github.com/gustavoem/intelligent-systems-project/blob/main/server/README.md).
