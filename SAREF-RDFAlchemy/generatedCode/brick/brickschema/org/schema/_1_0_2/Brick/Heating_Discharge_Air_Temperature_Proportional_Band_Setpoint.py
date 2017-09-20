from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature_Heating_Setpoint import Discharge_Air_Temperature_Heating_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature_Heating_Setpoint import Supply_Air_Temperature_Heating_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Proportional_Band_Setpoint import Proportional_Band_Setpoint


class Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint(Discharge_Air_Temperature_Heating_Setpoint,Supply_Air_Temperature_Heating_Setpoint,Proportional_Band_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint
	
	
