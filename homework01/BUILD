load("@rules_python//python:defs.bzl", "py_library", "py_test")

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
    srcs = ["read_animals.py"]
)

py_test(
    name = "read_animals_test",
    srcs = ["read_animals_test.py"],
    deps = [
        ":generate_animals",
        ":read_animals"
    ],
)
