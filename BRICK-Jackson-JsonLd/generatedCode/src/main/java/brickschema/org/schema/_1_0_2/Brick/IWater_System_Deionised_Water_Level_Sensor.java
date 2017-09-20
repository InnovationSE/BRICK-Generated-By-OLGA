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

import brickschema.org.schema._1_0_2.Brick.IDI_Water_Level_Sensor;  
import brickschema.org.schema._1_0_2.Brick.IDeionised_Water_Level_Sensor;  


public interface IWater_System_Deionised_Water_Level_Sensor extends IDI_Water_Level_Sensor, IDeionised_Water_Level_Sensor {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
