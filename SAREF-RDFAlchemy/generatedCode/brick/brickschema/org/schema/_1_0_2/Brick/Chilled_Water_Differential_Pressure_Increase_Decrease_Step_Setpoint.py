from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Increase_Decrease_Step_Setpoint import Increase_Decrease_Step_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Differential_Pressure_Setpoint import Chilled_Water_Differential_Pressure_Setpoint


class Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint(Increase_Decrease_Step_Setpoint,Chilled_Water_Differential_Pressure_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint
	
	
