# COE332
> Homeworks and assignments for COE322

![tests](https://github.com/alexwitt23/alw4364_coe332/workflows/tests/badge.svg)
----

This repo contains the homeworks and other assignments for COE322 taught in the
spring of 2021.

## Setup

Install the pip dependencies:

`python3 -m pip install -r requirements.txt`

The tests are defined as `Bazel` targets. `Bazelisk` is a clean way to
inferface with `Bazel`. It can be installed for `linux` machines as so:

```
# Install Bazelisk
pushd $(mktemp -d)
curl -fL -o bazel https://github.com/bazelbuild/bazelisk/releases/download/v1.7.4/bazelisk-linux-amd64
chmod +x bazel
sudo mv bazel /usr/local/bin
popd
```
You can check the latest available version for various devices
[here](https://github.com/bazelbuild/bazelisk/releases).

`Bazelisk` will read the `Bazel` version in `bazelversion`.


## Test

All tests can be run like so:

`bazel test //...`
