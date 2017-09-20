from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CO2_Level_Sensor import CO2_Level_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.VAV_CO2_Sensor import VAV_CO2_Sensor


class VAV_CO2_Level_Sensor(CO2_Level_Sensor,VAV_CO2_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_CO2_Level_Sensor
	
	
