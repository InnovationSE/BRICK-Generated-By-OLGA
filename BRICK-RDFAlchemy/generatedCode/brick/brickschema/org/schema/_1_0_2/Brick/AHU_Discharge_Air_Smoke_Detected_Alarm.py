from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Smoke_Detected_Alarm import Discharge_Air_Smoke_Detected_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Smoke_Detected_Alarm import Supply_Air_Smoke_Detected_Alarm


class AHU_Discharge_Air_Smoke_Detected_Alarm(Discharge_Air_Smoke_Detected_Alarm,Supply_Air_Smoke_Detected_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Discharge_Air_Smoke_Detected_Alarm
	
	
