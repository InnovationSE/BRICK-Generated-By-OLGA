from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Water_Temperature import Discharge_Water_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Water_Discharge_Temperature import Water_Discharge_Temperature


class Hot_Water_Discharge_Temperature(Discharge_Water_Temperature,Water_Discharge_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Discharge_Temperature
	
	
