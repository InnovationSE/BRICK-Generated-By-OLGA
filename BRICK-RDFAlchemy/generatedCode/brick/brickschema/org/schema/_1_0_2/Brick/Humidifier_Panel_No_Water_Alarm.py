from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Humidifier_Alarm import Humidifier_Alarm


class Humidifier_Panel_No_Water_Alarm(Humidifier_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Humidifier_Panel_No_Water_Alarm
	
	
