from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature_Cooling import Supply_Air_Temperature_Cooling


class Cooling_Coil_Supply_Air_Temperature(Supply_Air_Temperature_Cooling):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Coil_Supply_Air_Temperature
	
	
