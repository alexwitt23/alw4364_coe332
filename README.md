# COE332
![Tests](https://github.com/alexwitt23/alw4364_coe332/workflows/tests/badge.svg)
----

This repo contains the homeworks and other assignments for COE322 taught in the
spring of 2021.

## Setup

The tests are defined as `Bazel` rules. `Bazelisk` is a clean way to use `Bazel`:

```
python3 -m pip install -r requirements.txt

# Install Bazelisk
pushd $(mktemp -d)
curl -fL -o bazel https://github.com/bazelbuild/bazelisk/releases/download/v1.7.4/bazelisk-linux-amd64
chmod +x bazel
sudo mv bazel /usr/local/bin
popd
```

`Bazelisk` will read the `Bazel` version in `.bazelversion`.


## Test

All tests can be run like so:
```
bazel test //...
```
