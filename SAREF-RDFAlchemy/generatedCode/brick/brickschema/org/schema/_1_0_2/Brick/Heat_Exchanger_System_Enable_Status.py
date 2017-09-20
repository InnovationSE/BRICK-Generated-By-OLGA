from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.System_Status import System_Status
from brick.brickschema.org.schema._1_0_2.Brick.Enable_Status import Enable_Status


class Heat_Exchanger_System_Enable_Status(System_Status,Enable_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heat_Exchanger_System_Enable_Status
	
	
