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


import brickschema.org.schema._1_0_2.Brick.Hot_Water;
import brickschema.org.schema._1_0_2.Brick.Water;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Shutdown_Command;
import brickschema.org.schema._1_0_2.Brick.Command;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Shutdown_Hot_Water_When_Unoccupied_Command implements IShutdown_Hot_Water_When_Unoccupied_Command {

	IRI newInstance;
	
	public Shutdown_Hot_Water_When_Unoccupied_Command(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Shutdown_Hot_Water_When_Unoccupied_Command"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
