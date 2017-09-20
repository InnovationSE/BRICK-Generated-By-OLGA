from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature_Heating import Supply_Air_Temperature_Heating


class Heating_Supply_Air_Temperature_Proportional_Band(Supply_Air_Temperature_Heating):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Supply_Air_Temperature_Proportional_Band
	
	
