from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop import Start_Stop
from brick.brickschema.org.schema._1_0_2.Brick.Domestic_Hot_Water import Domestic_Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.System import System


class Domestic_Hot_Water_System_Start_Stop(Start_Stop,Domestic_Hot_Water,System):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Domestic_Hot_Water_System_Start_Stop
	
	
