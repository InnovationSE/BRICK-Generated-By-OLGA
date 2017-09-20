from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CWS import CWS
from brick.brickschema.org.schema._1_0_2.Brick.Coil import Coil


class Cooling_Coil(CWS,Coil):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Coil
	
	
