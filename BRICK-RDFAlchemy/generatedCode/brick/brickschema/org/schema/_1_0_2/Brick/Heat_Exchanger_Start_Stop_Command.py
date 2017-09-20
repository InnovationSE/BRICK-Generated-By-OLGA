from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop import Start_Stop
from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop_Command import Start_Stop_Command


class Heat_Exchanger_Start_Stop_Command(Start_Stop,Start_Stop_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heat_Exchanger_Start_Stop_Command
	
	
