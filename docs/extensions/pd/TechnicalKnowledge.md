---
search:
  boost: 10.0
---

# Class: TechnicalKnowledge 


_Information about the technical knowledge_



<div data-search-exclude markdown="1">



URI: [pd:TechnicalKnowledge](https://w3id.org/lmodel/dpv/pd/TechnicalKnowledge)





```mermaid
 classDiagram
    class TechnicalKnowledge
    click TechnicalKnowledge href "../TechnicalKnowledge/"
      KnowledgeBelief <|-- TechnicalKnowledge
        click KnowledgeBelief href "../KnowledgeBelief/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [KnowledgeBelief](KnowledgeBelief.md)
        * **TechnicalKnowledge**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:TechnicalKnowledge](https://w3id.org/lmodel/dpv/pd/TechnicalKnowledge) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Technical Knowledge




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#TechnicalKnowledge |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:TechnicalKnowledge |
| native | pd:TechnicalKnowledge |
| exact | dpv_pd:TechnicalKnowledge, dpv_pd_owl:TechnicalKnowledge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TechnicalKnowledge
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TechnicalKnowledge
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the technical knowledge
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Technical Knowledge
exact_mappings:
- dpv_pd:TechnicalKnowledge
- dpv_pd_owl:TechnicalKnowledge
is_a: KnowledgeBelief
class_uri: pd:TechnicalKnowledge

```
</details>

### Induced

<details>
```yaml
name: TechnicalKnowledge
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TechnicalKnowledge
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the technical knowledge
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Technical Knowledge
exact_mappings:
- dpv_pd:TechnicalKnowledge
- dpv_pd_owl:TechnicalKnowledge
is_a: KnowledgeBelief
class_uri: pd:TechnicalKnowledge

```
</details></div>