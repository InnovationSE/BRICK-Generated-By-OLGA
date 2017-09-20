from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Humidifier import Humidifier


class Humidifier_Panel_No_Water(Humidifier):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Humidifier_Panel_No_Water
	
	
