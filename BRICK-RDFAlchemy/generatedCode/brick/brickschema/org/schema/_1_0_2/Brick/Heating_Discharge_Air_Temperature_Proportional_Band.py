from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature_Heating import Discharge_Air_Temperature_Heating


class Heating_Discharge_Air_Temperature_Proportional_Band(Discharge_Air_Temperature_Heating):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Discharge_Air_Temperature_Proportional_Band
	
	
