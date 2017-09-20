from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Low_Temperature_Alarm import Low_Temperature_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Return_Air import Return_Air


class Return_Air_Temperature_Low_Limit_Alarm(Low_Temperature_Alarm,Return_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Air_Temperature_Low_Limit_Alarm
	
	
