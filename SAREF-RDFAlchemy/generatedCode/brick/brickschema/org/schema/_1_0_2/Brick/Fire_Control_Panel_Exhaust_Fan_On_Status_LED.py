from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fire_Control_Panel_LED_Status import Fire_Control_Panel_LED_Status
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_On_Status_LED import Exhaust_Fan_On_Status_LED


class Fire_Control_Panel_Exhaust_Fan_On_Status_LED(Fire_Control_Panel_LED_Status,Exhaust_Fan_On_Status_LED):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fire_Control_Panel_Exhaust_Fan_On_Status_LED
	
	
