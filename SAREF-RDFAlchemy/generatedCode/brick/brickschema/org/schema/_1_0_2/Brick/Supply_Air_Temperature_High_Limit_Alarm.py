from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature_Alarm import High_Temperature_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air import Discharge_Air
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air import Supply_Air


class Supply_Air_Temperature_High_Limit_Alarm(High_Temperature_Alarm,Discharge_Air,Supply_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Air_Temperature_High_Limit_Alarm
	
	
