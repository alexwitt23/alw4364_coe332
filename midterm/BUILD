package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library", "py_test")


py_library(
    name = "app",
    srcs = ["app.py"],
    deps = ["//homework02:generate_animals"]
)

py_test(
    name = "app_test",
    srcs = ["app_test.py"],
    deps = [":app"],
)
