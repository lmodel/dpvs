---
search:
  boost: 10.0
---

# Class: GPSCoordinate 


_Information about location expressed using Global Position System_

_coordinates (GPS)_



<div data-search-exclude markdown="1">



URI: [pd:GPSCoordinate](https://w3id.org/lmodel/dpv/pd/GPSCoordinate)





```mermaid
 classDiagram
    class GPSCoordinate
    click GPSCoordinate href "../GPSCoordinate/"
      DpvLocation <|-- GPSCoordinate
        click DpvLocation href "../DpvLocation/"
      CurrentLocation <|-- GPSCoordinate
        click CurrentLocation href "../CurrentLocation/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * [CurrentLocation](CurrentLocation.md)
            * **GPSCoordinate** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:GPSCoordinate](https://w3id.org/lmodel/dpv/pd/GPSCoordinate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* GPS Coordinate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#GPSCoordinate |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:GPSCoordinate |
| native | pd:GPSCoordinate |
| exact | dpv_pd:GPSCoordinate, dpv_pd_owl:GPSCoordinate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GPSCoordinate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#GPSCoordinate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about location expressed using Global Position System

  coordinates (GPS)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- GPS Coordinate
exact_mappings:
- dpv_pd:GPSCoordinate
- dpv_pd_owl:GPSCoordinate
is_a: CurrentLocation
mixins:
- DpvLocation
class_uri: pd:GPSCoordinate

```
</details>

### Induced

<details>
```yaml
name: GPSCoordinate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#GPSCoordinate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about location expressed using Global Position System

  coordinates (GPS)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- GPS Coordinate
exact_mappings:
- dpv_pd:GPSCoordinate
- dpv_pd_owl:GPSCoordinate
is_a: CurrentLocation
mixins:
- DpvLocation
class_uri: pd:GPSCoordinate

```
</details></div>