from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Water_Temperature_Setpoint import Supply_Water_Temperature_Setpoint


class Load_Shed_Supply_Water_Temperature_Setpoint(Supply_Water_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Load_Shed_Supply_Water_Temperature_Setpoint
	
	
