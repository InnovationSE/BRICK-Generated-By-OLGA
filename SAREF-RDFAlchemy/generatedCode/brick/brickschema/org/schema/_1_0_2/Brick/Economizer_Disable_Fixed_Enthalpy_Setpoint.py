from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Enthalpy_Setpoint import Economizer_Enthalpy_Setpoint


class Economizer_Disable_Fixed_Enthalpy_Setpoint(Economizer_Enthalpy_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Disable_Fixed_Enthalpy_Setpoint
	
	
