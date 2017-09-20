from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temporary_Occupancy_Status import Temporary_Occupancy_Status
from brick.brickschema.org.schema._1_0_2.Brick.VAV_Occupancy_Status import VAV_Occupancy_Status


class VAV_Temporary_Occupancy_Status(Temporary_Occupancy_Status,VAV_Occupancy_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Temporary_Occupancy_Status
	
	
