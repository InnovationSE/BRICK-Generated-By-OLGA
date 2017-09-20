from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.DemandResponse_Load_Shed_Command import DemandResponse_Load_Shed_Command
from brick.brickschema.org.schema._1_0_2.Brick.Standby_Load_Shed_Command import Standby_Load_Shed_Command


class DemandResponse_Standby_Load_Shed_Command(DemandResponse_Load_Shed_Command,Standby_Load_Shed_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').DemandResponse_Standby_Load_Shed_Command
	
	
