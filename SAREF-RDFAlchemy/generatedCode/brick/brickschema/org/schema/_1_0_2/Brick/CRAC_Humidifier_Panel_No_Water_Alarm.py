from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Humidifier_Panel_No_Water_Alarm import Humidifier_Panel_No_Water_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Humidifier_Alarm import CRAC_Humidifier_Alarm


class CRAC_Humidifier_Panel_No_Water_Alarm(Humidifier_Panel_No_Water_Alarm,CRAC_Humidifier_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Humidifier_Panel_No_Water_Alarm
	
	
