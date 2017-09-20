from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Static_Pressure_Dead_Band_Setpoint import Discharge_Air_Static_Pressure_Dead_Band_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Static_Pressure_Setpoint import AHU_Supply_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Static_Pressure_Setpoint import AHU_Discharge_Air_Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Static_Pressure_Dead_Band_Setpoint import Supply_Air_Static_Pressure_Dead_Band_Setpoint


class AHU_Supply_Air_Static_Pressure_Dead_Band_Setpoint(Discharge_Air_Static_Pressure_Dead_Band_Setpoint,AHU_Supply_Air_Static_Pressure_Setpoint,AHU_Discharge_Air_Static_Pressure_Setpoint,Supply_Air_Static_Pressure_Dead_Band_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Supply_Air_Static_Pressure_Dead_Band_Setpoint
	
	
