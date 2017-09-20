from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Low_Suction_Pressure_Alarm import Low_Suction_Pressure_Alarm


class CRAC_Low_Suction_Pressure_Alarm(Low_Suction_Pressure_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Low_Suction_Pressure_Alarm
	
	
