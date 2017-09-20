from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_On_Status_LED import AHU_On_Status_LED
from brick.brickschema.org.schema._1_0_2.Brick.Fire_Control_Panel_LED_Status import Fire_Control_Panel_LED_Status


class Fire_Control_Panel_AHU_On_Status_LED(AHU_On_Status_LED,Fire_Control_Panel_LED_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fire_Control_Panel_AHU_On_Status_LED
	
	
