from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop_Status import Start_Stop_Status
from brick.brickschema.org.schema._1_0_2.Brick.On_Off_Status import On_Off_Status


class Boiler_Start_Stop_Status(Start_Stop_Status,On_Off_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Boiler_Start_Stop_Status
	
	
