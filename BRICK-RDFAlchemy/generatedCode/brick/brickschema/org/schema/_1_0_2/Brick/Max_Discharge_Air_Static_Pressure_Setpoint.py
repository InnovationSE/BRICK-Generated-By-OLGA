from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Static_Pressure_Setpoint import Discharge_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Static_Pressure_Setpoint import Supply_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure_Max_Setpoint import Static_Pressure_Max_Setpoint


class Max_Discharge_Air_Static_Pressure_Setpoint(Discharge_Air_Static_Pressure_Setpoint,Supply_Air_Static_Pressure_Setpoint,Static_Pressure_Max_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Max_Discharge_Air_Static_Pressure_Setpoint
	
	
