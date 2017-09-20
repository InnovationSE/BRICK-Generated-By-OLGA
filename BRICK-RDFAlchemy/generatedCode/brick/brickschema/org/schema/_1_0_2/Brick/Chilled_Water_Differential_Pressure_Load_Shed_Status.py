from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Differential_Pressure_Load_Shed_Status import Differential_Pressure_Load_Shed_Status
from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water import Chilled_Water


class Chilled_Water_Differential_Pressure_Load_Shed_Status(Differential_Pressure_Load_Shed_Status,Chilled_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Differential_Pressure_Load_Shed_Status
	
	
