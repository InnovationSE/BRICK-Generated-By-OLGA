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


import brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Disable_Command;
import brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Command;
import brickschema.org.schema._1_0_2.Brick.Fan_Command;
import brickschema.org.schema._1_0_2.Brick.Command;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Disable;
import brickschema.org.schema._1_0_2.Brick.Exhaust_Fan;
import brickschema.org.schema._1_0_2.Brick.Fan;
import brickschema.org.schema._1_0_2.Brick.HVAC;
import brickschema.org.schema._1_0_2.Brick.Equipment;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Disable_Command;
import brickschema.org.schema._1_0_2.Brick.Command;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class AHU_Exhaust_Fan_Disable_Command implements IAHU_Exhaust_Fan_Disable_Command {

	IRI newInstance;
	
	public AHU_Exhaust_Fan_Disable_Command(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#AHU_Exhaust_Fan_Disable_Command"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}