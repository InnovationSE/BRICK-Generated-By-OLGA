from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Overridden_On_Status import AHU_Overridden_On_Status
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Overridden_On_Status import Exhaust_Fan_Overridden_On_Status
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Exhaust_Fan_Status import AHU_Exhaust_Fan_Status


class AHU_Exhaust_Fan_Overridden_On_Status(AHU_Overridden_On_Status,Exhaust_Fan_Overridden_On_Status,AHU_Exhaust_Fan_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Exhaust_Fan_Overridden_On_Status
	
	
