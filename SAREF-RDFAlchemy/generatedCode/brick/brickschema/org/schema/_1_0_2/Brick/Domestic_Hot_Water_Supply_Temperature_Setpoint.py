from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Supply_Temperature_Setpoint import Hot_Water_Supply_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Water_Temperature_Setpoint import Discharge_Water_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Domestic_Hot_Water import Domestic_Hot_Water


class Domestic_Hot_Water_Supply_Temperature_Setpoint(Hot_Water_Supply_Temperature_Setpoint,Discharge_Water_Temperature_Setpoint,Domestic_Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Domestic_Hot_Water_Supply_Temperature_Setpoint
	
	
