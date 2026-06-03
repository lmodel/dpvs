---
search:
  boost: 10.0
---

# Class: Thought 


_Information about thoughts_



<div data-search-exclude markdown="1">



URI: [pd:Thought](https://w3id.org/lmodel/dpv/pd/Thought)





```mermaid
 classDiagram
    class Thought
    click Thought href "../Thought/"
      KnowledgeBelief <|-- Thought
        click KnowledgeBelief href "../KnowledgeBelief/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [KnowledgeBelief](KnowledgeBelief.md)
        * **Thought**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Thought](https://w3id.org/lmodel/dpv/pd/Thought) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Thought




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Thought |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Thought |
| native | pd:Thought |
| exact | dpv_pd:Thought, dpv_pd_owl:Thought |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Thought
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Thought
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about thoughts
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Thought
exact_mappings:
- dpv_pd:Thought
- dpv_pd_owl:Thought
is_a: KnowledgeBelief
class_uri: pd:Thought

```
</details>

### Induced

<details>
```yaml
name: Thought
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Thought
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about thoughts
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Thought
exact_mappings:
- dpv_pd:Thought
- dpv_pd_owl:Thought
is_a: KnowledgeBelief
class_uri: pd:Thought

```
</details></div>