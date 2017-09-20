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

import brickschema.org.schema._1_0_2.Brick.IAHU_Discharge_Air_Static_Pressure_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IAHU_Supply_Air_Static_Pressure_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.IDischarge_Air_Static_Pressure_Integral_Time_Setpoint;  
import brickschema.org.schema._1_0_2.Brick.ISupply_Air_Static_Pressure_Integral_Time_Setpoint;  


public interface IAHU_Discharge_Air_Static_Pressure_Integral_Time_Setpoint extends IAHU_Discharge_Air_Static_Pressure_Setpoint, IAHU_Supply_Air_Static_Pressure_Setpoint, IDischarge_Air_Static_Pressure_Integral_Time_Setpoint, ISupply_Air_Static_Pressure_Integral_Time_Setpoint {

	/**
	* @return RefId
	*/
	@JsonIgnore
	public RefId getRefId();
	
	
}
