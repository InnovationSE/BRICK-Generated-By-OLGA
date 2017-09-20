from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Short_Cycle_Alarm import Short_Cycle_Alarm


class CRAC_Short_Cycle_Alarm(Short_Cycle_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Short_Cycle_Alarm
	
	
