# Homework 02

Enhancements to Homework 01 and Dockerizing.


## Installation

Check the root `README` for instructions for cloning and getting the environment
setup.

## Running the Code

As per the requirements for this project, you can choose to add the files
in `homework02` to your path so they can be invoked simply from their filenames.
If you do not want to permanatly add them to your path, run, from the _repo root_ like so:

```bash
PATH=$PATH:homework02 generate_animals.py \
    --animals_save_path homework02/animals.json
```

The above script `generate_animals.py` generates 20 random  Dr. Moreau-esk animals.
The animals are saved to a json at the path specified by `--animals_save_path`.

To read back a random animal from the collection and print some summary statistics,
pass `read_animal.py` your json file:

```bash
PATH=$PATH:homework02 read_animals.py \
    --animals_json_path homework02/animals.json
```


## Docker Image

You can build a Docker image using the provided in this Dockerfile. NOTE: this command expects you to be in the _root_ of the repo, not the _homework02_ folder:

#### Building

```bash
docker build -f homework02/Dockerfile -t coe332-homework02 .
```

#### Running
When running the container, a volume mount (`-v`) can be supplied so the output file of
`generate_animals.py` is stored on your local machine. Here is a command to mount
this repository's root path into a folder called `/data` within the container.

We then tell `generate_animals.py` to write the output file into `/data` on within
the _container_ which is really mapped to our current local directory.

```bash
docker run --rm -v $PWD:/data coe332-homework02:latest generate_animals.py \
    --animals_save_path /data/homework02/animals.json
```
You should now see  `homework02/animals.json` exists within your local copy of this
repo.

A random animal can be read from this generated file with the following command:
```bash
docker run --rm -v $PWD:/data coe332-homework02:latest read_animals.py \
    --animals_json_path /data/homework02/animals.json
```

If you'd like to enter the container and poke around, run:

```
docker run --rm -ti coe332-homework02:latest /bin/bash
```

## Test

All tests are set to run through bazel. Please see the instructions on the README.md
at the root of the repo for installing bazel (it's easy). Once you have run
the installation commands, to test everything run from the repo root:

```bash
bazel test //...
```

If you really don't like bazel or want to install it, you can run the python
unittests with `pytest`:

```
PYTHONPATH=. PY_IGNORE_IMPORTMISMATCH=1 pytest -q -s --doctest-modules --ignore-glob="bazel-*"
```

## Docker with Bazel
Docker is an amazing resource for packaging applications for distribution; however, it is not entirely hermetic. Bazel developers have created a system
to address these shortcommings, and I've used their rules to develop a virtually
identical image to what is produced with through the `Dockerfile`.

To build the image through bazel, run:

```
bazel run //homework02:coe322_bazel_docker
```

When that finishes, you should see two images have been created:

```
$ docker images
REPOSITORY              TAG                           IMAGE ID       CREATED          SIZE
bazel/homework02        coe322_bazel_docker_install   0dab7e6db88a   19 minutes ago   444MB
alexwitt23/homework02   coe322_bazel_docker           c1e004c9a85d   51 years ago     444MB
```

The `*_install` image is where we've installed the dependencies needed to run our
code.
You can now run the container with docker just like the container above:

```bash
docker run -ti --rm -v $PWD:/data alexwitt23/homework02:coe322_bazel_docker generate_animals.py \
    --animals_save_path /data/homework02/animals.json
docker run -ti --rm -v $PWD:/data alexwitt23/homework02:coe322_bazel_docker read_animals.py \
    --animals_json_path /data/homework02/animals.json
```

There is also a target that pushes the bazel-built image to `DockerHub`:
