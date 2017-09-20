from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature_Setpoint import Supply_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature_Setpoint import Discharge_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Temperature_Setpoint import Economizer_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Dead_Band_Setpoint import Dead_Band_Setpoint


class Economizer_Discharge_Air_Temperature_Dead_Band_Setpoint(Supply_Air_Temperature_Setpoint,Discharge_Air_Temperature_Setpoint,Economizer_Temperature_Setpoint,Dead_Band_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Discharge_Air_Temperature_Dead_Band_Setpoint
	
	
