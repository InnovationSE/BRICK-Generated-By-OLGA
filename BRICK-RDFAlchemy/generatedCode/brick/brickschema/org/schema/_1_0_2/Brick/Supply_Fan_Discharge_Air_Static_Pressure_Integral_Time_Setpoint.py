from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Static_Pressure_Integral_Time_Setpoint import Discharge_Air_Static_Pressure_Integral_Time_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Static_Pressure_Integral_Time_Setpoint import Supply_Air_Static_Pressure_Integral_Time_Setpoint


class Supply_Fan_Discharge_Air_Static_Pressure_Integral_Time_Setpoint(Discharge_Air_Static_Pressure_Integral_Time_Setpoint,Supply_Air_Static_Pressure_Integral_Time_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Fan_Discharge_Air_Static_Pressure_Integral_Time_Setpoint
	
	
