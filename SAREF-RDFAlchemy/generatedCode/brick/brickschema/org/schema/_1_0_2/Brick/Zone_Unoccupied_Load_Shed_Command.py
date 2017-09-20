from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Unoccupied_Load_Shed_Command import Unoccupied_Load_Shed_Command


class Zone_Unoccupied_Load_Shed_Command(Unoccupied_Load_Shed_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Zone_Unoccupied_Load_Shed_Command
	
	
