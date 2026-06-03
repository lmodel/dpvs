---
search:
  boost: 10.0
---

# Class: KnowledgeBelief 


_Information about knowledge and beliefs_



<div data-search-exclude markdown="1">



URI: [pd:KnowledgeBelief](https://w3id.org/lmodel/dpv/pd/KnowledgeBelief)





```mermaid
 classDiagram
    class KnowledgeBelief
    click KnowledgeBelief href "../KnowledgeBelief/"
      Internal <|-- KnowledgeBelief
        click Internal href "../Internal/"
      

      KnowledgeBelief <|-- PhilosophicalBelief
        click PhilosophicalBelief href "../PhilosophicalBelief/"
      KnowledgeBelief <|-- ReligiousBelief
        click ReligiousBelief href "../ReligiousBelief/"
      KnowledgeBelief <|-- TechnicalKnowledge
        click TechnicalKnowledge href "../TechnicalKnowledge/"
      KnowledgeBelief <|-- Thought
        click Thought href "../Thought/"
      

      
```





## Inheritance
* [Internal](Internal.md)
    * **KnowledgeBelief**
        * [TechnicalKnowledge](TechnicalKnowledge.md)
        * [Thought](Thought.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:KnowledgeBelief](https://w3id.org/lmodel/dpv/pd/KnowledgeBelief) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Knowledge and Beliefs




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#KnowledgeBelief |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:KnowledgeBelief |
| native | pd:KnowledgeBelief |
| exact | dpv_pd:KnowledgeBelief, dpv_pd_owl:KnowledgeBelief |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KnowledgeBelief
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#KnowledgeBelief
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about knowledge and beliefs
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Knowledge and Beliefs
exact_mappings:
- dpv_pd:KnowledgeBelief
- dpv_pd_owl:KnowledgeBelief
is_a: Internal
class_uri: pd:KnowledgeBelief

```
</details>

### Induced

<details>
```yaml
name: KnowledgeBelief
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#KnowledgeBelief
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about knowledge and beliefs
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Knowledge and Beliefs
exact_mappings:
- dpv_pd:KnowledgeBelief
- dpv_pd_owl:KnowledgeBelief
is_a: Internal
class_uri: pd:KnowledgeBelief

```
</details></div>