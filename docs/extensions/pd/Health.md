---
search:
  boost: 10.0
---

# Class: Health 


_Information about health_



<div data-search-exclude markdown="1">



URI: [pd:Health](https://w3id.org/lmodel/dpv/pd/Health)





```mermaid
 classDiagram
    class Health
    click Health href "../Health/"
      MedicalHealth <|-- Health
        click MedicalHealth href "../MedicalHealth/"
      

      Health <|-- Genetic
        click Genetic href "../Genetic/"
      Health <|-- MentalHealth
        click MentalHealth href "../MentalHealth/"
      Health <|-- PhysicalHealth
        click PhysicalHealth href "../PhysicalHealth/"
      

      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **Health**
        * [Genetic](Genetic.md)
        * [MentalHealth](MentalHealth.md)
        * [PhysicalHealth](PhysicalHealth.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Health](https://w3id.org/lmodel/dpv/pd/Health) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Health




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Health |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Health |
| native | pd:Health |
| exact | dpv_pd:Health, dpv_pd_owl:Health |
| related | svd:Health |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Health
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Health
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Health
exact_mappings:
- dpv_pd:Health
- dpv_pd_owl:Health
related_mappings:
- svd:Health
is_a: MedicalHealth
class_uri: pd:Health

```
</details>

### Induced

<details>
```yaml
name: Health
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Health
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Health
exact_mappings:
- dpv_pd:Health
- dpv_pd_owl:Health
related_mappings:
- svd:Health
is_a: MedicalHealth
class_uri: pd:Health

```
</details></div>