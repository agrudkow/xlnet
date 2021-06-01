import csv
from f1_metrics import F1Metrics
from pearson_metrics import PearsonMetrics

def load_files_to_metrics(predicted_path, target_path):
    predicted_file = open(predicted_path)
    target_file = open(target_path)

    predicted_types, predicted_scores = read_predicted(predicted_file)

    target_types, target_scores, tokens = read_target(target_file)

    return F1Metrics(predicted_types, predicted_scores, target_types, target_scores, tokens),\
           PearsonMetrics(predicted_types, predicted_scores, target_types, target_scores)


def read_predicted(predicted_file):
    reader = csv.reader(predicted_file, delimiter='\t')
    next(reader)
    predicted_types = []
    predicted_scores = []

    for row in reader:
        type, score = row[1].split("-")
        predicted_types.append(type)
        predicted_scores.append(int(score))

    return predicted_types, predicted_scores

def read_target(target_file):
    reader = csv.reader(target_file, delimiter='\t')
    target_types = []
    target_scores = []
    tokens = []

    for row in reader:
        type, score = row[0].split("-")
        target_types.append(type)
        target_scores.append(int(score))
        tokens.append(int(row[3]))

    return target_types, target_scores, tokens
