from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Smoke_Detected_Alarm import Smoke_Detected_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air import Supply_Air
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air import Discharge_Air


class Discharge_Air_Smoke_Detected_Alarm(Smoke_Detected_Alarm,Supply_Air,Discharge_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Discharge_Air_Smoke_Detected_Alarm
	
	
