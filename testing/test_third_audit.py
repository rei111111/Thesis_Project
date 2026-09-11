"""Independent effect-size regressions from the audit of archive 7020171c."""

import unittest

import numpy as np
import pandas as pd
from scipy.stats import rankdata

from evaluation.feature_associations import association_statistics


def reported_effect(labels, values):
    table = association_statistics(
        pd.DataFrame({"label": labels, "feature": values}),
        population="regression_fixture",
        bootstrap_resamples=3,
        seed=42,
        feature_names=("feature",),
    )
    return float(table.iloc[0]["kruskal_epsilon_squared"])


class ThirdAuditTests(unittest.TestCase):
    def test_epsilon_squared_matches_variance_explained_by_average_ranks(self):
        examples = (
            (np.repeat([1, 2, 3, 4], 2), [1, 3, 2, 4, 3, 5, 4, 6]),
            (np.repeat([1, 2, 3, 4], [5, 3, 4, 2]), [0, 0, 2, 4, 7, 2, 5, 5, 1, 2, 2, 9, 4, 8]),
            (np.repeat([1, 2, 3, 4], 3), np.repeat([10, 20, 30, 40], 3)),
            (np.repeat([1, 2, 3, 4], 3), np.tile([10, 20, 30], 4)),
        )
        for labels, values in examples:
            with self.subTest(values=values):
                # An independent oracle: decompose average-rank variance,
                # without using the implementation's Kruskal H statistic.
                ranks = rankdata(values, method="average")
                total = np.square(ranks - ranks.mean()).sum()
                between = sum(
                    np.count_nonzero(labels == label)
                    * (ranks[labels == label].mean() - ranks.mean()) ** 2
                    for label in np.unique(labels)
                )
                self.assertAlmostEqual(reported_effect(labels, values), between / total, places=12)

    def test_epsilon_squared_is_invariant_to_repeating_the_whole_sample(self):
        labels = np.repeat([1, 2, 3, 4], 2)
        values = np.array([1, 3, 2, 4, 3, 5, 4, 6])
        original = reported_effect(labels, values)
        repeated = reported_effect(np.tile(labels, 7), np.tile(values, 7))
        self.assertAlmostEqual(original, repeated, places=12)


if __name__ == "__main__":
    unittest.main()
