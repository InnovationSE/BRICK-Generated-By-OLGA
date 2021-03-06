from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.DI_Water_Alarm import DI_Water_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Deionised_Water_Alarm import Deionised_Water_Alarm


class Water_System_DI_Water_Alarm(DI_Water_Alarm,Deionised_Water_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Water_System_DI_Water_Alarm
	
	
