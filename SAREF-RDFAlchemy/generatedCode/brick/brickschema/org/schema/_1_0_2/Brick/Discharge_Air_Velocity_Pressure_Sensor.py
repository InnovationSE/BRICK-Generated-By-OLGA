from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Velocity_Pressure_Sensor import Velocity_Pressure_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air import Supply_Air
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air import Discharge_Air


class Discharge_Air_Velocity_Pressure_Sensor(Velocity_Pressure_Sensor,Supply_Air,Discharge_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Discharge_Air_Velocity_Pressure_Sensor
	
	
