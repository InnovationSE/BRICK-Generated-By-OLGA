from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Enthalpy_Setpoint import Enthalpy_Setpoint


class Economizer_Enthalpy_Setpoint(Enthalpy_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Enthalpy_Setpoint
	
	
