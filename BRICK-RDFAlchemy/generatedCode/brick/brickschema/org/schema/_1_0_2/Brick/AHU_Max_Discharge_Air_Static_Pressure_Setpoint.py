from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Max_Discharge_Air_Static_Pressure_Setpoint import Max_Discharge_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Static_Pressure_Setpoint import AHU_Supply_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Max_Supply_Air_Static_Pressure_Setpoint import Max_Supply_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Static_Pressure_Setpoint import Discharge_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Static_Pressure_Setpoint import AHU_Discharge_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Static_Pressure_Max_Setpoint import AHU_Static_Pressure_Max_Setpoint


class AHU_Max_Discharge_Air_Static_Pressure_Setpoint(Max_Discharge_Air_Static_Pressure_Setpoint,AHU_Supply_Air_Static_Pressure_Setpoint,Max_Supply_Air_Static_Pressure_Setpoint,Discharge_Air_Static_Pressure_Setpoint,AHU_Discharge_Air_Static_Pressure_Setpoint,AHU_Static_Pressure_Max_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Max_Discharge_Air_Static_Pressure_Setpoint
	
	
