from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Thermal_Power import Thermal_Power
from brick.brickschema.org.schema._1_0_2.Brick.Cooling import Cooling


class Cooling_Thermal_Power(Thermal_Power,Cooling):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Thermal_Power
	
	
