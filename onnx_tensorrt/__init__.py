# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import

import pkg_resources

from . import backend

__version__ = "8.2.1"
try:
    # The version is defined in setup.py
    __version__ = pkg_resources.require("onnx_tensorrt")[0].version
except pkg_resources.DistributionNotFound:
    __version__ = None
