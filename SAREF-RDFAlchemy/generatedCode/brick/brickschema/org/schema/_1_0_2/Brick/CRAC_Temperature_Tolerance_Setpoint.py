from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Temperature_Setpoint import CRAC_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Tolerance_Setpoint import Temperature_Tolerance_Setpoint


class CRAC_Temperature_Tolerance_Setpoint(CRAC_Temperature_Setpoint,Temperature_Tolerance_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Temperature_Tolerance_Setpoint
	
	
