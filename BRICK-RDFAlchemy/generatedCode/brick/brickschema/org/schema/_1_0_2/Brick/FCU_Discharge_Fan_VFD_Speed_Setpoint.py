from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_VFD_Speed_Setpoint import Discharge_Fan_VFD_Speed_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_VFD_Speed_Setpoint import Supply_Fan_VFD_Speed_Setpoint


class FCU_Discharge_Fan_VFD_Speed_Setpoint(Discharge_Fan_VFD_Speed_Setpoint,Supply_Fan_VFD_Speed_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_Discharge_Fan_VFD_Speed_Setpoint
	
	
