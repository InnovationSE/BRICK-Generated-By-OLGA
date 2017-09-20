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

import brickschema.org.schema._1_0_2.Brick.ISupply_Fan_Piezoelectric_Sensor;  
import brickschema.org.schema._1_0_2.Brick.IDischarge_Fan_Piezoelectric_Sensor;  


public interface IAHU_Supply_Fan_Piezoelectric_Sensor extends ISupply_Fan_Piezoelectric_Sensor, IDischarge_Fan_Piezoelectric_Sensor {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
