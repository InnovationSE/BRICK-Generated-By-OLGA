from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_System_Status import AHU_System_Status
from brick.brickschema.org.schema._1_0_2.Brick.System_Shutdown_Status import System_Shutdown_Status


class AHU_System_Shutdown_Status(AHU_System_Status,System_Shutdown_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_System_Shutdown_Status
	
	
