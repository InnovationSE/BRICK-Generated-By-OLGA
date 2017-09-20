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


import brickschema.org.schema._1_0_2.Brick.HWS_Discharge_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Supply_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Discharge_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Hot_Water_Supply_Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Discharge_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water;
import brickschema.org.schema._1_0_2.Brick.Hot_Water;
import brickschema.org.schema._1_0_2.Brick.Water;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Hot_Water_Supply_Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.HWS_Supply_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Discharge_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Supply_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Hot_Water_Supply_Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_High_Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Reset_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Discharge_Water_Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint;
import brickschema.org.schema._1_0_2.Brick.Setpoint;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water;
import brickschema.org.schema._1_0_2.Brick.Hot_Water;
import brickschema.org.schema._1_0_2.Brick.Water;
import brickschema.org.schema._1_0_2.Brick.Resource;
import brickschema.org.schema._1_0_2.Brick.Point;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
import brickschema.org.schema._1_0_2.Brick.UndefinedMeasurement;
import brickschema.org.schema._1_0_2.Brick.MeasurementProperty;
import brickschema.org.schema._1_0_2.BrickFrame.TagSet;
	


public  class HWS_Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint implements IHWS_Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint {

	IRI newInstance;
	
	public HWS_Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint(String namespace, String instanceId) {
		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(newInstance, RDF.TYPE, GLOBAL.factory.createIRI("https://brickschema.org/schema/1.0.2/Brick#HWS_Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	
	
}
