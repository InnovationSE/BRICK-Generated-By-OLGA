/**
* This file is automatically generated by OLGA
* @author OLGA
* @version 1.0
*/

package brickschema.org.schema._1_0_2.Brick;

import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;

import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldId;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldProperty;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldType;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldLink;
import ioinformarics.oss.jackson.module.jsonld.annotation.JsonldPropertyType;

import brick.jsonld.util.RefId;

import brickschema.org.schema._1_0_2.Brick.IHWS_Hot_Water_Supply_Temperature_Sensor;  
import brickschema.org.schema._1_0_2.Brick.IHot_Water_Supply_Temperature_Sensor;  
import brickschema.org.schema._1_0_2.Brick.IMedium_Temperature_Hot_Water_Supply_Temperature_Sensor;  
import brickschema.org.schema._1_0_2.Brick.IHWS_Hot_Water_Discharge_Temperature_Sensor;  
import brickschema.org.schema._1_0_2.Brick.IMedium_Temperature_Hot_Water_Discharge_Temperature_Sensor;  


public interface IHWS_Medium_Temperature_Hot_Water_Discharge_Temperature_Sensor extends IHWS_Hot_Water_Supply_Temperature_Sensor, IHot_Water_Supply_Temperature_Sensor, IMedium_Temperature_Hot_Water_Supply_Temperature_Sensor, IHWS_Hot_Water_Discharge_Temperature_Sensor, IMedium_Temperature_Hot_Water_Discharge_Temperature_Sensor {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
