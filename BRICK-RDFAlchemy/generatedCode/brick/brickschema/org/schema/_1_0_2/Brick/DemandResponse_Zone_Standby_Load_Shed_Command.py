from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Zone_Standby_Load_Shed_Command import Zone_Standby_Load_Shed_Command
from brick.brickschema.org.schema._1_0_2.Brick.DemandResponse_Standby_Load_Shed_Command import DemandResponse_Standby_Load_Shed_Command


class DemandResponse_Zone_Standby_Load_Shed_Command(Zone_Standby_Load_Shed_Command,DemandResponse_Standby_Load_Shed_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').DemandResponse_Zone_Standby_Load_Shed_Command
	
	
