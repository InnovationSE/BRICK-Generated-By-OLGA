from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Temperature import Heating_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Air_Temperature import Air_Temperature


class Open_Heating_Valve_Air_Temperature(Heating_Temperature,Air_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Open_Heating_Valve_Air_Temperature
	
	
