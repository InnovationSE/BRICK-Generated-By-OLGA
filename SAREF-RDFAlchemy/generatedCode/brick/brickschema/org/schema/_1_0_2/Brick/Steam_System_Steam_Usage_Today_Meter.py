from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Steam_Usage_Today_Meter import Steam_Usage_Today_Meter


class Steam_System_Steam_Usage_Today_Meter(Steam_Usage_Today_Meter):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Steam_System_Steam_Usage_Today_Meter
	
	
