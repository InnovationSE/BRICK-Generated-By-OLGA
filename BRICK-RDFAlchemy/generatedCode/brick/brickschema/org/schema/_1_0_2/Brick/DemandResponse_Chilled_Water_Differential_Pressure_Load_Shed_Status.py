from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Differential_Pressure_Load_Shed_Status import Chilled_Water_Differential_Pressure_Load_Shed_Status
from brick.brickschema.org.schema._1_0_2.Brick.DemandResponse_Load_Shed_Status import DemandResponse_Load_Shed_Status


class DemandResponse_Chilled_Water_Differential_Pressure_Load_Shed_Status(Chilled_Water_Differential_Pressure_Load_Shed_Status,DemandResponse_Load_Shed_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').DemandResponse_Chilled_Water_Differential_Pressure_Load_Shed_Status
	
	
