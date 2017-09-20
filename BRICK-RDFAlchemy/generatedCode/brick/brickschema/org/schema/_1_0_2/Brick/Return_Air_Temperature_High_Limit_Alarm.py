from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature_Alarm import High_Temperature_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Return_Air import Return_Air


class Return_Air_Temperature_High_Limit_Alarm(High_Temperature_Alarm,Return_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Air_Temperature_High_Limit_Alarm
	
	
