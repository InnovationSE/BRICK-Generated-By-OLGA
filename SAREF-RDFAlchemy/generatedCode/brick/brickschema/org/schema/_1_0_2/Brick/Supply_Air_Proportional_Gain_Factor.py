from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air import Supply_Air
from brick.brickschema.org.schema._1_0_2.Brick.Proportional_Gain_Setpoint import Proportional_Gain_Setpoint


class Supply_Air_Proportional_Gain_Factor(Supply_Air,Proportional_Gain_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Air_Proportional_Gain_Factor
	
	
