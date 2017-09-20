from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Pump import Hot_Water_Pump
from brick.brickschema.org.schema._1_0_2.Brick.Lead_Lag import Lead_Lag


class Hot_Water_Pump_Lead_Lag(Hot_Water_Pump,Lead_Lag):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Pump_Lead_Lag
	
	
