---
search:
  boost: 10.0
---

# Class: MentalHealth 


_Information about mental health_



<div data-search-exclude markdown="1">



URI: [pd:MentalHealth](https://w3id.org/lmodel/dpv/pd/MentalHealth)





```mermaid
 classDiagram
    class MentalHealth
    click MentalHealth href "../MentalHealth/"
      Health <|-- MentalHealth
        click Health href "../Health/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * [Health](Health.md)
        * **MentalHealth**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:MentalHealth](https://w3id.org/lmodel/dpv/pd/MentalHealth) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Mental Health




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#MentalHealth |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:MentalHealth |
| native | pd:MentalHealth |
| exact | dpv_pd:MentalHealth, dpv_pd_owl:MentalHealth |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MentalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MentalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about mental health
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Mental Health
exact_mappings:
- dpv_pd:MentalHealth
- dpv_pd_owl:MentalHealth
is_a: Health
class_uri: pd:MentalHealth

```
</details>

### Induced

<details>
```yaml
name: MentalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MentalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about mental health
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Mental Health
exact_mappings:
- dpv_pd:MentalHealth
- dpv_pd_owl:MentalHealth
is_a: Health
class_uri: pd:MentalHealth

```
</details></div>