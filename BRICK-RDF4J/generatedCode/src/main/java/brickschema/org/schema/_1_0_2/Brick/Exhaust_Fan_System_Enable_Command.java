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


import brickschema.org.schema._1_0_2.Brick.System_Enable_Command;
import brickschema.org.schema._1_0_2.Brick.Enable_Command;
import brickschema.org.schema._1_0_2.Brick.Command;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Enable_Command;
import brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Command;
import brickschema.org.schema._1_0_2.Brick.Fan_Command;
import brickschema.org.schema._1_0_2.Brick.Command;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Enable_Command;
import brickschema.org.schema._1_0_2.Brick.Command;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Exhaust_Fan_System_Enable_Command implements IExhaust_Fan_System_Enable_Command {

	IRI newInstance;
	
	public Exhaust_Fan_System_Enable_Command(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Exhaust_Fan_System_Enable_Command"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
