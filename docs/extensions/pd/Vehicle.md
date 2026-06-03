---
search:
  boost: 10.0
---

# Class: Vehicle 


_Information about vehicles_



<div data-search-exclude markdown="1">



URI: [pd:Vehicle](https://w3id.org/lmodel/dpv/pd/Vehicle)





```mermaid
 classDiagram
    class Vehicle
    click Vehicle href "../Vehicle/"
      External <|-- Vehicle
        click External href "../External/"
      

      Vehicle <|-- VehicleLicense
        click VehicleLicense href "../VehicleLicense/"
      Vehicle <|-- VehicleUsage
        click VehicleUsage href "../VehicleUsage/"
      

      
```





## Inheritance
* [External](External.md)
    * **Vehicle**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Vehicle](https://w3id.org/lmodel/dpv/pd/Vehicle) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Vehicle




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Vehicle |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Vehicle |
| native | pd:Vehicle |
| exact | dpv_pd:Vehicle, dpv_pd_owl:Vehicle |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vehicle
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Vehicle
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicles
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle
exact_mappings:
- dpv_pd:Vehicle
- dpv_pd_owl:Vehicle
is_a: External
class_uri: pd:Vehicle

```
</details>

### Induced

<details>
```yaml
name: Vehicle
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Vehicle
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicles
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle
exact_mappings:
- dpv_pd:Vehicle
- dpv_pd_owl:Vehicle
is_a: External
class_uri: pd:Vehicle

```
</details></div>