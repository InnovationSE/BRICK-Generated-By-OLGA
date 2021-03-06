from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Discharge_Air_Flow_Setpoint import Cooling_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Unoccupied_Cooling_Supply_Air_Flow_Setpoint import Unoccupied_Cooling_Supply_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Discharge_Air_Flow_Setpoint import VAV_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Unoccupied_Cooling_Discharge_Air_Flow_Setpoint import Unoccupied_Cooling_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Supply_Air_Flow_Setpoint import VAV_Supply_Air_Flow_Setpoint


class VAV_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint(Cooling_Discharge_Air_Flow_Setpoint,Unoccupied_Cooling_Supply_Air_Flow_Setpoint,VAV_Discharge_Air_Flow_Setpoint,Unoccupied_Cooling_Discharge_Air_Flow_Setpoint,VAV_Supply_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint
	
	
