---
search:
  boost: 10.0
---

# Class: PhilosophicalBelief 


_Information about philosophical beliefs_



<div data-search-exclude markdown="1">



URI: [pd:PhilosophicalBelief](https://w3id.org/lmodel/dpv/pd/PhilosophicalBelief)





```mermaid
 classDiagram
    class PhilosophicalBelief
    click PhilosophicalBelief href "../PhilosophicalBelief/"
      KnowledgeBelief <|-- PhilosophicalBelief
        click KnowledgeBelief href "../KnowledgeBelief/"
      
      
```





## Inheritance
* **PhilosophicalBelief** [ [KnowledgeBelief](KnowledgeBelief.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PhilosophicalBelief](https://w3id.org/lmodel/dpv/pd/PhilosophicalBelief) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Philosophical Belief




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PhilosophicalBelief |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PhilosophicalBelief |
| native | pd:PhilosophicalBelief |
| exact | dpv_pd:PhilosophicalBelief, dpv_pd_owl:PhilosophicalBelief |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhilosophicalBelief
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PhilosophicalBelief
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about philosophical beliefs
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Philosophical Belief
exact_mappings:
- dpv_pd:PhilosophicalBelief
- dpv_pd_owl:PhilosophicalBelief
mixins:
- KnowledgeBelief
class_uri: pd:PhilosophicalBelief

```
</details>

### Induced

<details>
```yaml
name: PhilosophicalBelief
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PhilosophicalBelief
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about philosophical beliefs
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Philosophical Belief
exact_mappings:
- dpv_pd:PhilosophicalBelief
- dpv_pd_owl:PhilosophicalBelief
mixins:
- KnowledgeBelief
class_uri: pd:PhilosophicalBelief

```
</details></div>