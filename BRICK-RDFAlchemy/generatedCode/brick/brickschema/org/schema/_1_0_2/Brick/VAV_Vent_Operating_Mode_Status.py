from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Vent_Operating_Mode_Status import Vent_Operating_Mode_Status


class VAV_Vent_Operating_Mode_Status(Vent_Operating_Mode_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Vent_Operating_Mode_Status
	
	