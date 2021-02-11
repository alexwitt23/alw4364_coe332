package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library", "py_test")
load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
    "container_push",
)
load("@io_bazel_rules_docker//python:image.bzl", "py_layer")
load("@io_bazel_rules_docker//docker/util:run.bzl", "container_run_and_commit")


py_library(
    name = "generate_animals",
    srcs = ["generate_animals.py"]
)

py_test(
    name = "generate_animals_test",
    srcs = ["generate_animals_test.py"],
    deps = [":generate_animals"],
)

py_library(
    name = "read_animals",
    srcs = ["read_animals.py"],
)

py_library(
    name = "homework02_src",
    deps = [
        ":generate_animals",
        ":read_animals",
    ],
)

py_test(
    name = "read_animals_test",
    srcs = ["read_animals_test.py"],
    deps = [
        ":generate_animals",
        ":read_animals",
    ],
)

sh_test(
    name = "dockerfile_test",
    size = "large",  # 300 Mb RAM and 15 min timeout
    srcs = ["docker_test.sh"],
    data = [
        "Dockerfile",
        ":homework02_src"
    ],
    local = True,
)

# Install python and the petname package. Do this first as the
# yum install can take a while and we'd like the built to remain
# quick when just changing the files in this repo.
container_run_and_commit(
    name = "coe322_bazel_docker_install",
    commands = [
        "yum update -y && yum install -y python3",
        "rm -rf /var/cache/yum",
        "python3 -m pip install --upgrade pip petname==2.2",
    ],
    image = "@centos7.7.1908//image",
)

# Add our source files onto our prepared centos image.
container_image(
    name = "coe322_bazel_docker",
    base = ":coe322_bazel_docker_install",
    files = [
        ":generate_animals",
        ":read_animals",
    ],
    directory = "/build",  # Where `files` are put
    workdir = "/home",  # same as WORKDIR in Dockerfile
    repository = "alexwitt23",
    symlinks = {
        "/usr/local/bin/generate_animals.py": "/build/generate_animals.py",
        "/usr/local/bin/read_animals.py": "/build/read_animals.py",
    },
)

# Push the docker image to Docker Hub. Invoke this target with `bazel run`
# to actually push it.
container_push(
    name = "push_coe322_bazel_docker",
    format = "Docker",
    image = ":coe322_bazel_docker.tar",
    registry = "index.docker.io",
    repository = "alexwitt23/json-parser-bazel",
    tag = "latest"
)
