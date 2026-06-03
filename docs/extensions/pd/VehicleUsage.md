---
search:
  boost: 10.0
---

# Class: VehicleUsage 


_Information about usage of vehicles, e.g. driving statistics_



<div data-search-exclude markdown="1">



URI: [pd:VehicleUsage](https://w3id.org/lmodel/dpv/pd/VehicleUsage)





```mermaid
 classDiagram
    class VehicleUsage
    click VehicleUsage href "../VehicleUsage/"
      Vehicle <|-- VehicleUsage
        click Vehicle href "../Vehicle/"
      Behavioural <|-- VehicleUsage
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **VehicleUsage** [ [Vehicle](Vehicle.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:VehicleUsage](https://w3id.org/lmodel/dpv/pd/VehicleUsage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Vehicle Usage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#VehicleUsage |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:VehicleUsage |
| native | pd:VehicleUsage |
| exact | dpv_pd:VehicleUsage, dpv_pd_owl:VehicleUsage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VehicleUsage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicleUsage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about usage of vehicles, e.g. driving statistics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle Usage
exact_mappings:
- dpv_pd:VehicleUsage
- dpv_pd_owl:VehicleUsage
is_a: Behavioural
mixins:
- Vehicle
class_uri: pd:VehicleUsage

```
</details>

### Induced

<details>
```yaml
name: VehicleUsage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicleUsage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about usage of vehicles, e.g. driving statistics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle Usage
exact_mappings:
- dpv_pd:VehicleUsage
- dpv_pd_owl:VehicleUsage
is_a: Behavioural
mixins:
- Vehicle
class_uri: pd:VehicleUsage

```
</details></div>