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

import brickschema.org.schema._1_0_2.Brick.IDischarge_Air_Temperature_Cooling_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.ISupply_Air_Temperature_Cooling_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IAHU_Discharge_Air_Temperature_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IAHU_Supply_Air_Temperature_Setpoint;  


public interface IAHU_Discharge_Air_Temperature_Cooling_Setpoint extends IDischarge_Air_Temperature_Cooling_Setpoint, ISupply_Air_Temperature_Cooling_Setpoint, IAHU_Discharge_Air_Temperature_Setpoint, IAHU_Supply_Air_Temperature_Setpoint {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
