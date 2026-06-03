---
search:
  boost: 10.0
---

# Class: Personality 


_Information about personality (e.g., categorization in terms of the Big_

_Five personality traits)_



<div data-search-exclude markdown="1">



URI: [pd:Personality](https://w3id.org/lmodel/dpv/pd/Personality)





```mermaid
 classDiagram
    class Personality
    click Personality href "../Personality/"
      Behavioural <|-- Personality
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **Personality**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Personality](https://w3id.org/lmodel/dpv/pd/Personality) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Personality




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Personality |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Personality |
| native | pd:Personality |
| exact | dpv_pd:Personality, dpv_pd_owl:Personality |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Personality
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Personality
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about personality (e.g., categorization in terms of the
  Big

  Five personality traits)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Personality
exact_mappings:
- dpv_pd:Personality
- dpv_pd_owl:Personality
is_a: Behavioural
class_uri: pd:Personality

```
</details>

### Induced

<details>
```yaml
name: Personality
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Personality
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about personality (e.g., categorization in terms of the
  Big

  Five personality traits)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Personality
exact_mappings:
- dpv_pd:Personality
- dpv_pd_owl:Personality
is_a: Behavioural
class_uri: pd:Personality

```
</details></div>