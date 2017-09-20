from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Valve import Heating_Valve
from brick.brickschema.org.schema._1_0_2.Brick.Domestic_Hot_Water import Domestic_Hot_Water


class Domestic_Hot_Water_Valve(Heating_Valve,Domestic_Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Domestic_Hot_Water_Valve
	
	
