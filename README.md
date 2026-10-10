# Organic Flow Battery Ontology (OFBO)

The **Organic Flow Battery Ontology (OFBO)** is an OWL ontology for representing molecular, electrochemical, computational, degradation, and provenance information relevant to organic redox flow battery research.

OFBO supports ontology-based data access (OBDA): curated relational data are exposed as a virtual RDF knowledge graph using Ontop, H2, and the OFBO mappings.

## Documentation

Human-readable documentation for OFBO, including ontology metadata, classes, object properties, datatype properties, annotation properties, and downloadable serializations, is available at:

<https://w3id.org/ofbo/>

The documentation is generated with [WIDOCO](https://w3id.org/widoco/) from the ontology source and is maintained in the `docs/` directory.

## Contents

- `ontology/` — OFBO ontology, Ontop mappings, configuration, and imported ontology modules.
- `docs/` — Generated human-readable ontology documentation, published at <https://w3id.org/ofbo/>.
- `database/csv/` — Curated source-data tables.
- `database/h2/` — H2 database and H2 JAR file.
- `database/triples/` — Materialized RDF graph.
- `case_studies/` — Jupyter notebooks and SPARQL queries for:
  - SPARQL-engine benchmarking;
  - competency-question evaluation;
  - pH-dependent redox-potential analysis;
  - expert-guided and KPI-based candidate selection; and
  - theoretical–experimental comparisons.
- `validation/` — Reasoning and validation outputs from SHACL and ROBOT.

## Main resources

| Resource | Description |
|---|---|
| `ontology/OFBO.ttl` | OFBO ontology in Turtle syntax. |
| `ontology/OFBO.obda` | Ontop OBDA mappings. |
| `ontology/OFBO.properties` | H2 database connection configuration for Ontop. |
| `docs/` | Generated WIDOCO documentation for OFBO. Available online at <https://w3id.org/ofbo/docs>. |
| `database/h2/ofbo_db.mv.db` | H2 database containing the curated data. |
| `database/h2/h2.jar` | H2 database engine. |
| `database/triples/OFBO-materialized.ttl` | Materialized RDF representation of the mapped graph. |
| `case_studies/competency_questions/` | Competency-question notebook and executable SPARQL queries. |
| `validation/ofbo-shapes.ttl` | SHACL validation shapes. |

## Ontology identifiers

- **Ontology IRI:** `https://w3id.org/ofbo`  
  The permanent identifier of the OFBO ontology.

- **Namespace:** `https://w3id.org/ofbo#`  
  The base namespace for OFBO terms, for example: `https://w3id.org/ofbo#OFBO_0001104`.

- **Preferred prefix:** `ofbo`

- **Current version:** `1.2.0`

- **Ontology document:** `https://w3id.org/ofbo/OFBO.ttl`  
  This is the Turtle file to use when importing or downloading the ontology.

- **Documentation:** `https://w3id.org/ofbo/`  
  This URL provides the human-readable ontology documentation.

## Requirements

Before running the notebooks or benchmark, ensure the following dependencies are available:

| Component | Version | Notes |
|---|---:|---|
| Python | 3.x | Required for the Jupyter notebooks and benchmark scripts |
| [Ontop](https://github.com/ontop/ontop/releases) | 5.5.0 | Provides the virtual SPARQL endpoint |
| [Apache Jena Fuseki](https://jena.apache.org/download/index.cgi) | 6.2.0 | Provides the materialized RDF SPARQL endpoint |
| H2 database | Included | Bundled as `database/h2/h2.jar` |

### Python dependencies

Install the packages required by the Jupyter notebooks:

## Running the H2 database

The database file is located at:

    database/h2/ofbo_db.mv.db

## Running the SPARQL endpoints

From the repository root, start Ontop and Fuseki before running the benchmark.

### Ontop

```bash
ontop endpoint --ontology=ontology/OFBO.ttl --mapping=ontology/OFBO.obda --properties=ontology/OFBO.properties
```

Endpoint: `http://localhost:8080/sparql`

### Fuseki

```bash
fuseki-server --file=database/triples/OFBO-materialized.ttl /ofbo
```

Endpoint: `http://localhost:3030/ofbo/query`

## Competency questions

The competency-question notebook and query files are available in:

    case_studies/competency_questions/

The queries demonstrate retrieval of information including molecular scaffolds, pH-dependent redox potentials, computational methods, degradation pathways, solubility, bromination compatibility, predicted properties, and paired experimental–computational data.

## Validation

OFBO was assessed using reasoning and SHACL validation. Relevant resources are available in:

- `validation/validation.ipynb`
- `validation/ofbo-shapes.ttl`
- `validation/reports/robot-report.tsv`
- `validation/reports/OFBO-reasoned.ttl`
- `validation/reports/shacl-report.ttl`

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