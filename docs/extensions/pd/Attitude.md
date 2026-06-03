---
search:
  boost: 10.0
---

# Class: Attitude 


_Information about attitude_



<div data-search-exclude markdown="1">



URI: [pd:Attitude](https://w3id.org/lmodel/dpv/pd/Attitude)





```mermaid
 classDiagram
    class Attitude
    click Attitude href "../Attitude/"
      Behavioural <|-- Attitude
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **Attitude**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Attitude](https://w3id.org/lmodel/dpv/pd/Attitude) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Attitude




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Attitude |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Attitude |
| native | pd:Attitude |
| exact | dpv_pd:Attitude, dpv_pd_owl:Attitude |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Attitude
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Attitude
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about attitude
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Attitude
exact_mappings:
- dpv_pd:Attitude
- dpv_pd_owl:Attitude
is_a: Behavioural
class_uri: pd:Attitude

```
</details>

### Induced

<details>
```yaml
name: Attitude
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Attitude
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about attitude
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Attitude
exact_mappings:
- dpv_pd:Attitude
- dpv_pd_owl:Attitude
is_a: Behavioural
class_uri: pd:Attitude

```
</details></div>