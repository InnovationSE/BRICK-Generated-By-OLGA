# OLGA: Ontology Library GenerAtor
 
OLGA is a generic tool aiming to accelerate the adoption of the Semantic technology such as the Ontology Web Language [OWL](https://www.w3.org/OWL) and the Resource Description Framework [RDF](https://www.w3.org/2001/sw/wiki/RDF), and Json Linked Data [Jsonld](https://json-ld.org/) in the Internet Of Things development.

OLGA complements existing OWL, RDF, and Jsonld serializers such as [Jackson-Jsonld in Java](https://github.com/io-informatics/jackson-jsonld) and [RDF4J](http://rdf4j.org/) or RDF Object Relational Mappers such as [RomanticWeb in C#](RomanticWeb.net) and [RDFAlchemy in Python](http://rdfalchemy.readthedocs.io/en/latest/index.html). 

OLGA takes as input the following:
1. One or more Ontologies
2. A paramter indicating the dependency of the generated library.
	1. Jackson-Jsonld - Java
	2. RomanticWeb - C#
	3. RDF4J - Java
	4. RDFAlchemy - Python

The output of OLGA is a generated library ready to be used by IoT developers. The generated library is conform to the ontology and is dependent on available serializers and ORMs in various languages (C#, Java, and Python for now)
