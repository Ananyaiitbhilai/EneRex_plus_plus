from glob import glob
from semanticscholar import SemanticScholar


# Example usage:
if __name__ == "__main__":
    files = glob("test_scirex/*.json")
    sch = SemanticScholar()
    urls = []
    for file in files:
        filename = file.split(".")[0].split("/")[-1]
        if glob(f"test_scirex/pdfs/{filename}.pdf"):
            continue
        paper = sch.get_paper(filename)
        access = paper.openAccessPdf
        if access:
            urls.append(f"wget -O test_scirex/pdfs/{filename}.pdf {access['url']}")
        else:
            print(file)
    with open("download_them.txt", "w") as f:
        for p in urls:
            f.write(p)
            f.write("\n")
