from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Flow_Command import Supply_Air_Flow_Command
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Flow_Command import Discharge_Air_Flow_Command


class VAV_Supply_Air_Flow_Command(Supply_Air_Flow_Command,Discharge_Air_Flow_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Supply_Air_Flow_Command
	
	
