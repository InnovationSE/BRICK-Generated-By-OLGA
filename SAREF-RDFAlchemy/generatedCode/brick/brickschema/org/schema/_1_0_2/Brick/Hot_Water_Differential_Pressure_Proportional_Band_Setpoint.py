from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Differential_Pressure_Proportional_Band_Setpoint import Differential_Pressure_Proportional_Band_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Differential_Pressure_Setpoint import Hot_Water_Differential_Pressure_Setpoint


class Hot_Water_Differential_Pressure_Proportional_Band_Setpoint(Differential_Pressure_Proportional_Band_Setpoint,Hot_Water_Differential_Pressure_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Differential_Pressure_Proportional_Band_Setpoint
	
	
