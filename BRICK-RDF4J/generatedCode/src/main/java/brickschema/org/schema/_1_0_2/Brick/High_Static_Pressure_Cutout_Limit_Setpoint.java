/**
* This file is automatically generated by OLGA
* @author OLGA
* @version 1.0
*/
package brickschema.org.schema._1_0_2.Brick;

import brick.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;

import java.math.BigDecimal;
import javax.xml.datatype.XMLGregorianCalendar;
import java.util.Date;


import brickschema.org.schema._1_0_2.Brick.Static_Pressure_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Pressure_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class High_Static_Pressure_Cutout_Limit_Setpoint implements IHigh_Static_Pressure_Cutout_Limit_Setpoint {

	IRI newInstance;
	
	public High_Static_Pressure_Cutout_Limit_Setpoint(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#High_Static_Pressure_Cutout_Limit_Setpoint"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
