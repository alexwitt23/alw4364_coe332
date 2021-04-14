package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library", "py_test")


py_library(
    name = "generate_animals",
    srcs = ["generate_animals.py"],
)

py_test(
    name = "generate_animals_test",
    srcs = ["generate_animals_test.py"],
    deps = [":generate_animals"]
)

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
    "container_push",
)
load("@io_bazel_rules_docker//docker/util:run.bzl", "container_run_and_commit")

# Install python and the petname package. Do this first as the
# yum install can take a while and we'd like the built to remain
# quick when just changing the files in this repo.
container_run_and_commit(
    name = "coe332_midterm_install",
    commands = [
        "yum update -y && yum install -y python3",
        "rm -rf /var/cache/yum",
        "python3 -m pip install --upgrade pip petname==2.2",
    ],
    image = "@centos7.7.1908//image",
)

# Add our source files onto our prepared centos image.
container_image(
    name = "coe332_midterm",
    base = ":coe332_midterm_install",
    files = [
        ":generate_animals",
    ],
    directory = "/build",  # Where `files` are put
    workdir = "/home",  # same as WORKDIR in Dockerfile
    repository = "alexwitt23",
    symlinks = {
        "/usr/local/bin/generate_animals.py": "/build/generate_animals.py",
    },
)

# Push the docker image to Docker Hub. Invoke this target with `bazel run`
# to actually push it.
container_push(
    name = "push_coe332_midterm",
    format = "Docker",
    image = ":coe332_midterm.tar",
    registry = "index.docker.io",
    repository = "alexwitt23/coe332-midterm",
    tag = "latest"
)
