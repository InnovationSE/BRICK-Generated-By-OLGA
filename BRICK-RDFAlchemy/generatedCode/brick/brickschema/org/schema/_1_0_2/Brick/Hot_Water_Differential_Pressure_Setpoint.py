from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Differential_Pressure_Setpoint import Differential_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water


class Hot_Water_Differential_Pressure_Setpoint(Differential_Pressure_Setpoint,Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Differential_Pressure_Setpoint
	
	
