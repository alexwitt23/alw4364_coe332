package(default_visibility = ["//visibility:public"])

exports_files(glob(["requirements.txt"]))

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
    "container_push",
    "container_layer",
)
load("@io_bazel_rules_docker//contrib:test.bzl", "container_test")
load("@io_bazel_rules_docker//docker/util:run.bzl", "container_run_and_commit")


container_layer(
    name = "python-deps",
    files = [
        "requirements.txt",
    ],
)

container_image(
    name = "coe332_hw07_base",
    base = "@python//image",
    files = [
        "requirements.txt",
    ],
    layers = [":python-deps"],
    directory = "/app",
    workdir = "/app",
)

container_run_and_commit(
    name = "coe332_hw07_install",
    commands = [
        "python3 -m pip install -r requirements.txt",
    ],
    image = ":coe332_hw07_base.tar",
)

container_image(
    name = "coe332_hw07",
    base = ":coe332_hw07_install_commit.tar",
    files = [
        "//homework07/src:api",
        "//homework07/src:jobs",
        "//homework07/src:worker",
    ],
    labels = {
        "desc": "Image for homework07",
        "version": "0.1",
    },
    directory = "/app",
    workdir = "/app",
    repository = "alexwitt23",
)

# Push the docker image to Docker Hub. Invoke this target with `bazel run`
# to actually push it.
container_push(
    name = "push_coe332_hw07",
    format = "Docker",
    image = ":coe332_hw07",
    registry = "index.docker.io",
    repository = "alexwitt23/coe332-hw07",
    tag = "latest"
)

# Test
container_test(
    name = "homework07_bazel_test",
    configs = ["//homework07/test_configs:homework07.yml"],
    image = ":coe332_hw07",
)
