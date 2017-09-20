from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Heating_Discharge_Air_Flow_Setpoint import Occupied_Heating_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Heating_Max_Discharge_Air_Flow_Setpoint import Occupied_Heating_Max_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Heating_Max_Supply_Air_Flow_Setpoint import VAV_Heating_Max_Supply_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Occupied_Heating_Supply_Air_Flow_Setpoint import VAV_Occupied_Heating_Supply_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Heating_Max_Discharge_Air_Flow_Setpoint import VAV_Heating_Max_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Occupied_Heating_Discharge_Air_Flow_Setpoint import VAV_Occupied_Heating_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Heating_Max_Supply_Air_Flow_Setpoint import Occupied_Heating_Max_Supply_Air_Flow_Setpoint


class VAV_Occupied_Heating_Max_Discharge_Air_Flow_Setpoint(Occupied_Heating_Discharge_Air_Flow_Setpoint,Occupied_Heating_Max_Discharge_Air_Flow_Setpoint,VAV_Heating_Max_Supply_Air_Flow_Setpoint,VAV_Occupied_Heating_Supply_Air_Flow_Setpoint,VAV_Heating_Max_Discharge_Air_Flow_Setpoint,VAV_Occupied_Heating_Discharge_Air_Flow_Setpoint,Occupied_Heating_Max_Supply_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Occupied_Heating_Max_Discharge_Air_Flow_Setpoint
	
	
