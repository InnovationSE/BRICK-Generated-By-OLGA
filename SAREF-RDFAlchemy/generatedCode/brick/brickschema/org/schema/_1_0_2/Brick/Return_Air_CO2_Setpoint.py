from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CO2_Setpoint import CO2_Setpoint


class Return_Air_CO2_Setpoint(CO2_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Air_CO2_Setpoint
	
	
