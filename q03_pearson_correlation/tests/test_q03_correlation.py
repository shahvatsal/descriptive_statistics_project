from unittest import TestCase
from ..build import correlation
from inspect import getargspec


class TestLoad_regression_plot(TestCase):
    def test_correlation(self):  # Input parameters tests
        args = getargspec(correlation)
        self.assertEqual(len(args[0]), 0, "Expected arguments %d, Given %d" % (0, len(args[0])))

    def test_correlation_default(self):  # Input parameters default
        args = getargspec(correlation)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_correlation_result_type(self):  # Return type tests
        corr = correlation()
        self.assertIsInstance(corr, float,
                              "Expected data type for Pearson correlation is float you are returning %s" % (type(corr)))

    def test_correlation_result_values(self):  # Return value tests
        corr = correlation()
        self.assertAlmostEqual(correlation(), 0.0487782084064, 3, "Return `Pearson correlation` value does not match\
         expected value")
