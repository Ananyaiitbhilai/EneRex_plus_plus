import json
import argparse


def get_dataset(input_file, output_dir):
    with open(input_file, "r") as f:
        files = f.readlines()

    for paper in files:
        data = json.loads(paper)
        basename = data["doc_id"]
        frontmatter = {
            "basename": basename,
        }
        sections = {}
        for i, section in enumerate(data["sections"]):
            start_word = section[0]
            end_word = section[1]
            content = " ".join(data["words"][start_word:end_word])
            if content.startswith("bibliography"):
                break
            if not content.startswith("figure"):
                sections[str(i)] = content

        with open(f"{output_dir}/{basename}.json", "w") as f:
            json.dump([frontmatter, sections], f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    args = parser.parse_args()
    get_dataset(args.input_file, args.output_dir)
