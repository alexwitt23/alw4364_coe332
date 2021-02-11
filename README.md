# COE332
> Homeworks and assignments for COE322

![tests](https://github.com/alexwitt23/alw4364_coe332/workflows/tests/badge.svg)
----

This repo contains the homeworks and other assignments for COE322 taught in the
spring of 2021.


## Setup

Install the python dependencies:

`python3 -m pip install -r requirements.txt`

The tests are defined as `Bazel` targets. `Bazelisk` is a clean way to
inferface with `Bazel`. It can be installed for `linux` machines as so:

```
# Install Bazelisk on Linux
pushd $(mktemp -d)
curl -fL -o bazel https://github.com/bazelbuild/bazelisk/releases/download/v1.7.4/bazelisk-linux-amd64
chmod +x bazel
sudo mv bazel /usr/local/bin
popd
```
You can check the latest available version for various devices
[here](https://github.com/bazelbuild/bazelisk/releases).

Bazelisk will read the Bazel version in `.bazelversion`.

You will also need to have Docker installed on your device to run the Bazel tests.


## Test

All tests can be run like so with Bazel:

```
bazel test //...
```

You can also run the tests with `pytest`:

```
PYTHONPATH=. PY_IGNORE_IMPORTMISMATCH=1 pytest -s --doctest-modules --ignore-glob="bazel-*"
```

## Continuous Integration

All Bazel test targets are run through a Github Actions workflow. You can
find this file in `.github/workflows/test.yaml`. Currently, Bazel is only run on
Linux systems. This is because Github Actions doesn't support native docker
on MacOS. The `pytest` command is still run on MacOS, though.
