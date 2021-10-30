# Server

In the second part of this project, we will create an **API** for the
**categorization model** developed previously.

More specifically, you will **develop a server** that should receive data
related to **products** and return the best **categories** for them using a
**pretrained model**.

More info about the data can be found [here][1].


## Input

The expected input for the server should follow the following schema:
```json
{
  "products": [
    {
      "title": "Lembrancinha",
      "query": "lembrancinha legal",
      "concatenated_tags": "lembancinha festa criança"
    },
    {
      "title": "Carrinho de Bebê"
    }
  ]
}
```
You can provide `title`, `query` and `concatenated_tags` for each
product, and they are not required; however, at least one of them should
be provided.

You'll find a json schema on `schemas.py` that you can use to validate
your data.

## Output

The output from the server follow the following schema:
```json
{
  "categories": [
    "Lembrancinha",
    "Bebê"
  ]
}
```

## Infrastructure

In this directory, we provide a **containerized environment** that uses
[docker][4] and [docker-compose][5] to run the API. This should standardize the
development environment and avoid compatibility problems.

To install docker and docker-compose, check their official documentation
[here][4] and [here][5]. Both tools should be instalable at Linux, MacOS and
Windows.

To execute the API, just run the following command:
```bash
docker-compose up --build
```
Then open the link shown in the end.

To install an OS package (Debian-based), add the name of the package in the file
`packages.txt`. To intall a Python package (Pip-based), add the name and version
of the package in the file `requirements.txt`.

## Running tests
You can access an interactive bash inside the container with the command

`run_bash.sh`

Once you're in the container, you can go to the tests directory

`cd tests`

And then you can run unittest to run all tests.

`python -m unittest discover` 


[1]: ../data/README.md
[2]: https://flask.palletsprojects.com/en/1.1.x/
[3]: https://realpython.com/documenting-python-code/
[4]: https://docs.docker.com/get-docker
[5]: https://docs.docker.com/compose/install
