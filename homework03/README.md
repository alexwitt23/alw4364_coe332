# Homework 03

In this homework, we containerize a flask application to read information from
the json data generated in homeworks 1 and 2. An API is created to access this
information.

## Setup

Building the docker container can be performed using the `docker-compose.yml`
file in this folder. Run `docker-compose` from this repository's root:

```bash
docker-compose -f homework03/docker-compose.yml up -d
```

The `-d` runs the docker container in the detached mode.

## API Usage

Once the container is running, you can query your local host on port `5038`.

#### Generating Animals

You can issue some curl commands like so to create an animals json:

```bash
curl "localhost:5038/create_animals"
```

This will create an `animals.json` filee in the docker container. You can also
specify a path where you want to save the json file. This is useful if you've
mounted a folder.

```bash
curl "localhost:5038/create_animals?path=/tmp/animals.json"
```

The number of animals generated can also be supplied:

```bash
curl "localhost:5038/create_animals?number=200"
```

#### Reading Animals

After creating animals, you can issue some curl commands like so to query to the
generated animals. This will print out all the animals in the file:

```bash
curl "localhost:5038/animals"
```

You can also collect the animals by their head type or number of legs:

```bash
curl "localhost:5038/animals?head=snake&legs=10"
```

## Example Script

After starting the docker container, you can run

```bash
./homework03/consumer.py
```

to run a few examples commands.
