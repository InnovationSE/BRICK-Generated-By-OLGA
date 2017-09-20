/**
* This file is automatically generated by OLGA
* @author OLGA
* @version 1.0
*/
package brickschema.org.schema._1_0_2.BrickFrame;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

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

import brickschema.org.schema._1_0_2.BrickFrame.IToken;  
import brickschema.org.schema._1_0_2.BrickFrame.Taggable;






public  class Label implements ILabel {

	Map<String, List<RefId>> relations;
	
	public Label(String id) {
		super();
		this.id = "https://brickschema.org/schema/1.0.2/BrickFrame#" + id;
		relations = new HashMap<String, List<RefId>>();
		hasTokenSomeToken = new ArrayList<>();
		
	}

	@JsonldId
	public String id;
	
	@JsonIgnore
	public RefId getRefId()
	{
		return new RefId(id);
	}
	
	@JsonInclude(Include.NON_NULL)
	@JsonProperty("@type")
	public String getType()
	{
		return "https://brickschema.org/schema/1.0.2/BrickFrame#Label";
	}
	
	@JsonInclude(Include.NON_EMPTY)
	@JsonldProperty("https://brickschema.org/schema/1.0.2/BrickFrame#hasToken") 
	private List<RefId> hasTokenSomeToken;
	public void addhasTokenSome(IToken parameter)
	{
		hasTokenSomeToken.add(parameter.getRefId());
	}
	
	
	
	
	@JsonInclude(Include.NON_EMPTY)
	@JsonProperty("https://brickschema.org/schema/1.0.2/BrickFrame#hasToken")
	public List<RefId> gethasTokenToken()
	{
		return hasTokenSomeToken;
	}
	
}