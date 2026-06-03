---
search:
  boost: 10.0
---

# Class: PhysicalHealth 


_Information about physical health_



<div data-search-exclude markdown="1">



URI: [pd:PhysicalHealth](https://w3id.org/lmodel/dpv/pd/PhysicalHealth)





```mermaid
 classDiagram
    class PhysicalHealth
    click PhysicalHealth href "../PhysicalHealth/"
      Health <|-- PhysicalHealth
        click Health href "../Health/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * [Health](Health.md)
        * **PhysicalHealth**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PhysicalHealth](https://w3id.org/lmodel/dpv/pd/PhysicalHealth) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Physical Health




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PhysicalHealth |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PhysicalHealth |
| native | pd:PhysicalHealth |
| exact | dpv_pd:PhysicalHealth, dpv_pd_owl:PhysicalHealth |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PhysicalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about physical health
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Physical Health
exact_mappings:
- dpv_pd:PhysicalHealth
- dpv_pd_owl:PhysicalHealth
is_a: Health
class_uri: pd:PhysicalHealth

```
</details>

### Induced

<details>
```yaml
name: PhysicalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PhysicalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about physical health
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Physical Health
exact_mappings:
- dpv_pd:PhysicalHealth
- dpv_pd_owl:PhysicalHealth
is_a: Health
class_uri: pd:PhysicalHealth

```
</details></div>