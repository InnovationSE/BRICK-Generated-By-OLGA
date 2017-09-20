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


import brickschema.org.schema._1_0_2.Brick.CWS;
import brickschema.org.schema._1_0_2.Brick.HVAC;
import brickschema.org.schema._1_0_2.Brick.Equipment;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Water_System;
import brickschema.org.schema._1_0_2.Brick.Equipment;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Chiller implements IChiller {

	IRI newInstance;
	
	public Chiller(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Chiller"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}