from rdflib import Graph
from pyshacl import validate


DATA_FILE = "../database/triples/OFBO-materialized.ttl"
SHAPES_FILE = "ofbo-shapes.ttl"
REPORT_FILE = "shacl-report.ttl"


def main():
    data_graph = Graph()
    data_graph.parse(DATA_FILE, format="turtle")

    shapes_graph = Graph()
    shapes_graph.parse(SHAPES_FILE, format="turtle")

    conforms, report_graph, report_text = validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        inference="none",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
        meta_shacl=True,
        advanced=True,
    )

    report_graph.serialize(destination=REPORT_FILE, format="turtle")

    print(report_text)
    print(f"\nSHACL report written to: {REPORT_FILE}")

    if conforms:
        print("\nRESULT: SHACL validation conforms.")
    else:
        print("\nRESULT: SHACL validation found violations.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()