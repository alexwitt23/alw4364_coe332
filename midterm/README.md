# Midterm

In this midterm, we compose a Flask application to read information from the json data
generated from a modified `generate_animals.py`. The animals are sent to a redis
database and an API is used to access the database items.

## Setup

Building these docker containers can be performed using the `docker-compose.yml` file
in this folder. Run `docker-compose` from this repository's _root_:

```bash
docker-compose -f midterm/docker-compose.yml up -d
```

The `-d` runs the docker container in the detached mode.

## API Usage

Once the container is running, you can query your local host on port `5038`.

#### Generating Animals

You must first issue a command to generate animals and populate the database. The
`create_animals` endpoint will generate 1 animal by default, or a desired number can be
specified.

```bash
curl "localhost:5038/create_animals?number=200"
```

The endpoint returns the animals generated so the user can see the uuid's for futher
manipulation.

#### Query Date Range

A list of animals created in some time range can be queried:

```bash
curl "localhost:5038/get_date_range?start=YYYY-MM-DDTHH:MM:SS&end=YYYY-MM-DDTHH:MM:SS"
```

The command does not have to have this much resolution, for example:

```bash
curl "localhost:5038/get_date_range?start=YYYY-MM-DDTHH:MM:SS&end=YYYY-MM-DD"
```

#### Edit Creature

If the uuid for a particular animal is known, new animal components can be supplied to
update the animal in the dataset.

```bash
curl "localhost:5038/update_animal?uuid=foo&body=bar&arms=var0&legs=var1&tails=var2&"
```


#### Remove Animals by Date of Birth

Animals can be removed from the database by specifying the start and end date range to
the endpoint `remove_by_date`.

```bash
curl "localhost:5038/remove_by_date?start=YYYY-MM-DDTHH:MM:SS&end=YYYY-MM-DDTHH:MM:SS"
```

#### Average Leg Count

The average number of legs across the animals can be found like so:

```bash
curl "localhost:5038/get_leg_average"
```

#### Total Number of Animals

See the number of animals like so:

```bash
curl "localhost:5038/get_num_animals"
```


#### See Animals

A command to see all the animals is:

```bash
curl "localhost:5038/get_animals"
```
