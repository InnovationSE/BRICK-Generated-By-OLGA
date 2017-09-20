from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Increase_Decrease_Step_Setpoint import Increase_Decrease_Step_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Static_Pressure_Setpoint import Supply_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Static_Pressure_Setpoint import Discharge_Air_Static_Pressure_Setpoint


class Supply_Air_Static_Pressure_Increase_Decrease_Step_Setpoint(Increase_Decrease_Step_Setpoint,Supply_Air_Static_Pressure_Setpoint,Discharge_Air_Static_Pressure_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Air_Static_Pressure_Increase_Decrease_Step_Setpoint
	
	
