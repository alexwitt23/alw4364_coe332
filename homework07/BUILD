package(default_visibility = ["//visibility:public"])

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
    "container_push",
)

container_image(
    name = "coe332_hw07",
    base = "@python//image",
    directory = "/build",
    workdir = "/home",
    repository = "alexwitt23",
)

# Push the docker image to Docker Hub. Invoke this target with `bazel run`
# to actually push it.
container_push(
    name = "push_coe332_hw07",
    format = "Docker",
    image = ":coe332_hw07.tar",
    registry = "index.docker.io",
    repository = "alexwitt23/coe332-hw07",
    tag = "latest"
)
