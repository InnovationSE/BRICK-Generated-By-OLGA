from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.On_Off_Status import On_Off_Status
from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop_Status import Start_Stop_Status


class Boiler_On_Off_Status(On_Off_Status,Start_Stop_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Boiler_On_Off_Status
	
	
