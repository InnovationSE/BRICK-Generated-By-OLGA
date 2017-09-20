from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Power_System import Power_System


class Demand_Response(Power_System):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Demand_Response
	
	
