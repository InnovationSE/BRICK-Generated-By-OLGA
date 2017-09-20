from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Pump import Chilled_Water_Pump
from brick.brickschema.org.schema._1_0_2.Brick.Pump_Start_Stop import Pump_Start_Stop


class Chilled_Water_Pump_Start_Stop(Chilled_Water_Pump,Pump_Start_Stop):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Pump_Start_Stop
	
	
