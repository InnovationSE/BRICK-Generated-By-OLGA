from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Domestic_Hot_Water import Domestic_Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Discharge_Temperature import Hot_Water_Discharge_Temperature


class Domestic_Hot_Water_Discharge_Temperature(Domestic_Hot_Water,Hot_Water_Discharge_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Domestic_Hot_Water_Discharge_Temperature
	
	
