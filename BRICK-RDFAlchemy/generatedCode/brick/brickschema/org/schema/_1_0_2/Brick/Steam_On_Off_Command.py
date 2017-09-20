from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.On_Off_Command import On_Off_Command
from brick.brickschema.org.schema._1_0_2.Brick.Steam import Steam


class Steam_On_Off_Command(On_Off_Command,Steam):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Steam_On_Off_Command
	
	