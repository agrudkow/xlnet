import math

TYPE_VALUE_MAP = {
    'EQUI': 5,
    'OPPO': 4,
    'SPE1': 3,
    'SPE2': 3,
    'SIMI': 2,
    'REL': 1
}

class PearsonMetrics:

    def __init__(self, predicted_types, predicted_scores, target_types, target_scores):
        self._predicted_types = predicted_types
        self._predicted_scores = predicted_scores
        self._target_types = target_types
        self._target_scores = target_scores

    def print_statistics(self):
        print("[Pearson Score], correlation for alignment type labels: {}".format(self.count_person_for_type()))
        print("[Pearson Type], correlation for alignment score labels: {}".format(self.count_pearson_for_score()))

    def count_person_for_type(self):
        mean_p = self.count_mean_for_type(self._predicted_types)
        mean_t = self.count_mean_for_type(self._target_types)

        return self.count_pearson(self.get_types_as_values(self._predicted_types), self.get_types_as_values(self._target_types),
                                  mean_p, mean_t)

    def count_mean_for_type(self, types):
        return self.count_mean(self.get_types_as_values(types))

    def count_pearson_for_score(self):
        mean_p = self.count_mean_score(self._predicted_scores)
        mean_t = self.count_mean_score(self._target_scores)

        return self.count_pearson(self._predicted_scores, self._target_scores, mean_p, mean_t)

    def count_mean_score(self, scores):
        return self.count_mean(scores)

    def count_pearson(self, predicted, target, mean_p, mean_t):
        sum_p = 0.
        sum_t = 0.
        up = 0.

        for i in range(len(predicted)):
            diff_p = predicted[i] - mean_p
            diff_t = target[i] - mean_t

            sum_p += diff_p ** 2
            sum_t += diff_t ** 2
            up += diff_p * diff_t

        sum_p = math.sqrt(sum_p)
        sum_t = math.sqrt(sum_t)

        return up / (sum_p * sum_t)

    def get_types_as_values(self, types):
        return list(map(TYPE_VALUE_MAP.get, types))

    def count_mean(self, values):
        sum_val = sum(values)
        return sum_val / len(values)
