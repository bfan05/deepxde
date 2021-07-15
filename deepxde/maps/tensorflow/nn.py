from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ...backend import tf


class NN(tf.keras.Model):
    """Map base class."""

    def __init__(self):
        super(NN, self).__init__()
        self.data_id = None
        self._inputs = None
        self._targets = None

        self.regularizer = None

        self._input_transform = None
        self._output_transform = None

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        self._inputs = value

    @property
    def targets(self):
        return self._targets

    @targets.setter
    def targets(self, value):
        self._targets = value

    def apply_feature_transform(self, transform):
        """Compute the features by appling a transform to the network inputs, i.e.,
        features = transform(inputs). Then, outputs = network(features).
        """
        self._input_transform = transform

    def apply_output_transform(self, transform):
        """Apply a transform to the network outputs, i.e.,
        outputs = transform(inputs, outputs).
        """
        self._output_transform = transform