from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint import Temperature_Setpoint


class Supply_Water_Temperature_Setpoint(Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Water_Temperature_Setpoint
	
	
