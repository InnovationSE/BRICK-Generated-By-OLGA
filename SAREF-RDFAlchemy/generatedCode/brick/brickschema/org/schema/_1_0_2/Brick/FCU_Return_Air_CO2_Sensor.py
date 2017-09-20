from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.FCU_CO2_Sensor import FCU_CO2_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Return_Air_CO2_Sensor import Return_Air_CO2_Sensor


class FCU_Return_Air_CO2_Sensor(FCU_CO2_Sensor,Return_Air_CO2_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_Return_Air_CO2_Sensor
	
	
