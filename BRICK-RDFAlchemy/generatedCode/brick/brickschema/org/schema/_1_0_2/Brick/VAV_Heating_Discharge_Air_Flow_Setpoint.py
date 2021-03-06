from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Discharge_Air_Flow_Setpoint import Heating_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Supply_Air_Flow_Setpoint import VAV_Supply_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Discharge_Air_Flow_Setpoint import VAV_Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Flow_Setpoint import Discharge_Air_Flow_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Heating_Supply_Air_Flow_Setpoint import Heating_Supply_Air_Flow_Setpoint


class VAV_Heating_Discharge_Air_Flow_Setpoint(Heating_Discharge_Air_Flow_Setpoint,VAV_Supply_Air_Flow_Setpoint,VAV_Discharge_Air_Flow_Setpoint,Discharge_Air_Flow_Setpoint,Heating_Supply_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Heating_Discharge_Air_Flow_Setpoint
	
	
