from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Proportional_Gain_Setpoint import Proportional_Gain_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Proportional_Gain_Factor import Supply_Air_Proportional_Gain_Factor


class AHU_Supply_Air_Proportional_Gain_Factor(Proportional_Gain_Setpoint,Supply_Air_Proportional_Gain_Factor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Supply_Air_Proportional_Gain_Factor
	
	
