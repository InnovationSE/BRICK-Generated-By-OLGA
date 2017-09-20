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


import brickschema.org.schema._1_0_2.Brick.Supply_Water_Differential_Pressure_Dead_Band_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Dead_Band_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint implements IThermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint {

	IRI newInstance;
	
	public Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
