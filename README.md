# Organic Flow Battery Ontology (OFBO)

The **Organic Flow Battery Ontology (OFBO)** is an OWL ontology for representing molecular, electrochemical, computational, degradation, and provenance information relevant to organic redox flow battery research.

OFBO supports ontology-based data access (OBDA): curated relational data are exposed as a virtual RDF knowledge graph using Ontop, H2, and the OFBO mappings.

## Contents

- `ontology/` — OFBO ontology, Ontop mappings, configuration, and imported ontology modules.
- `database/csv/` — Curated source-data tables.
- `database/h2/` — H2 database and H2 JAR file.
- `database/triples/` — Materialized RDF graph.
- `case_studies/` — Jupyter notebooks and SPARQL queries for:
  - SPARQL-engine benchmarking;
  - competency-question evaluation;
  - pH-dependent redox-potential analysis;
  - expert-guided and KPI-based candidate selection; and
  - theoretical–experimental comparisons.
- `shacl/` — SHACL shapes, validation report, and validation script.
- `validation/` — Reasoning and validation outputs.

## Main resources

| Resource | Description |
|---|---|
| `ontology/OFBO.ttl` | OFBO ontology in Turtle syntax. |
| `ontology/OFBO.obda` | Ontop OBDA mappings. |
| `ontology/OFBO.properties` | H2 database connection configuration for Ontop. |
| `database/h2/ofbo_db.mv.db` | H2 database containing the curated data. |
| `database/h2/h2.jar` | H2 database engine. |
| `database/triples/OFBO-materialized.ttl` | Materialized RDF representation of the mapped graph. |
| `case_studies/competency_questions/` | Competency-question notebook and executable SPARQL queries. |
| `shacl/ofbo-shapes.ttl` | SHACL validation shapes. |

## Ontology identifiers

- Ontology IRI: `https://w3id.org/ofbo`
- Namespace: `https://w3id.org/ofbo#`
- Preferred prefix: `ofbo`
- Current version: `1.2.0`

## Requirements

- Java
- Python 3
- Ontop 5.5.0
- H2 database, included as `database/h2/h2.jar`

To run the Jupyter notebooks, install the required Python packages:

    pip install jupyter pandas numpy requests matplotlib scipy rdflib networkx psutil pyshacl

Optional molecular-structure rendering in selected notebooks requires RDKit. Installation through Conda is recommended:

    conda install -c conda-forge rdkit

## Running the H2 database

From the repository root, start the H2 TCP server:

    java -cp database/h2/h2.jar org.h2.tools.Server -tcp -tcpAllowOthers -ifNotExists

The database file is located at:

    database/h2/ofbo_db.mv.db

## Running the Ontop endpoint

The notebooks expect an Ontop SPARQL endpoint at:

    http://localhost:8080/sparql

Start Ontop from the repository root using the ontology, mappings, and properties file:

    ontop endpoint --ontology=ontology/OFBO.ttl --mapping=ontology/OFBO.obda --properties=ontology/OFBO.properties

After Ontop has started, SPARQL queries can be submitted to:

    http://localhost:8080/sparql

## Competency questions

The competency-question notebook and query files are available in:

    case_studies/competency_questions/

The queries demonstrate retrieval of information including molecular scaffolds, pH-dependent redox potentials, computational methods, degradation pathways, solubility, bromination compatibility, predicted properties, and paired experimental–computational data.

## Validation

OFBO was assessed using reasoning and SHACL validation. Relevant resources include:

- `shacl/ofbo-shapes.ttl`
- `shacl/shacl-report.ttl`
- `shacl/validate_shacl.py`
- `validation/validation.ipynb`
- `validation/reports/robot-report.tsv`
- `validation/reports/OFBO-reasoned.ttl`

## Data provenance

The included CSV tables contain curated data derived from openly available literature sources. OFBO mappings associate property observations with molecular entities, experimental or computational processes, chemical systems, units, and primary publications.

## License

The ontology and repository resources are distributed under the terms specified in [`LICENSE`](LICENSE).

## Maintainer

**Daniel Willimetz**  
Fraunhofer Institute for Algorithms and Scientific Computing SCAI  
Email: [daniel.willimetz@scai.fraunhofer.de](mailto:daniel.willimetz@scai.fraunhofer.de)  
GitHub: [@dwillimetz](https://github.com/dwillimetz)  
ORCID: [0000-0001-9923-9676](https://orcid.org/0000-0001-9923-9676)

## Funding

OFBO was developed within the [PREDICTOR project](https://www.rfb-predictor.eu/), funded by the European Union under Grant Agreement No. 101168943.