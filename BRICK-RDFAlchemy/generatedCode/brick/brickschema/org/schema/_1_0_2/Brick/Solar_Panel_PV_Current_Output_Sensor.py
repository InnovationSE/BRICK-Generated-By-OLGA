from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.PV_Current_Output_Sensor import PV_Current_Output_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Photovoltaic_Current_Output_Sensor import Photovoltaic_Current_Output_Sensor


class Solar_Panel_PV_Current_Output_Sensor(PV_Current_Output_Sensor,Photovoltaic_Current_Output_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Solar_Panel_PV_Current_Output_Sensor
	
	
