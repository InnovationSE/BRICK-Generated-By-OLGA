/**
* This file is automatically generated by OLGA
* @author OLGA
* @version 1.0
*/

package brickschema.org.schema._1_0_2.BrickFrame;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;

import brickschema.org.schema._1_0_2.BrickFrame.ITaggable;  
import brickschema.org.schema._1_0_2.BrickFrame.IToken;  
import brickschema.org.schema._1_0_2.BrickFrame.ITagSet;  


public interface IToken extends ITaggable {


	public IRI iri();
			
	public void addHastag_Some(IToken parameter);
			
	public void addHastagset_Some(ITagSet parameter);
			
	
}