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
