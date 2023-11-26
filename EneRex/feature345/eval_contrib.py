import json
import argparse


def evaluate(jsonFile):
    with open(jsonFile, "r", encoding="utf-8") as f:
        data = json.load(f)

    mean_score = 0
    for doc_id, human_eval in data.items():
        score = 0
        for token in human_eval:
            if token == "1":
                score += 1
            else:
                score += 0
        score = score / len(human_eval)
        mean_score += score
        print(doc_id, score, sep="\t")
    print("Mean score:", mean_score / len(data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=str, required=True)
    args = parser.parse_args()
    evaluate(args.json)
