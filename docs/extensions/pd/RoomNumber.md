---
search:
  boost: 10.0
---

# Class: RoomNumber 


_Information about location expressed as room number or similar numbering_

_systems_



<div data-search-exclude markdown="1">



URI: [pd:RoomNumber](https://w3id.org/lmodel/dpv/pd/RoomNumber)





```mermaid
 classDiagram
    class RoomNumber
    click RoomNumber href "../RoomNumber/"
      DpvLocation <|-- RoomNumber
        click DpvLocation href "../DpvLocation/"
      PhysicalAddress <|-- RoomNumber
        click PhysicalAddress href "../PhysicalAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
            * **RoomNumber** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:RoomNumber](https://w3id.org/lmodel/dpv/pd/RoomNumber) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Room Number




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#RoomNumber |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:RoomNumber |
| native | pd:RoomNumber |
| exact | dpv_pd:RoomNumber, dpv_pd_owl:RoomNumber |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RoomNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#RoomNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about location expressed as room number or similar numbering

  systems'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Room Number
exact_mappings:
- dpv_pd:RoomNumber
- dpv_pd_owl:RoomNumber
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:RoomNumber

```
</details>

### Induced

<details>
```yaml
name: RoomNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#RoomNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about location expressed as room number or similar numbering

  systems'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Room Number
exact_mappings:
- dpv_pd:RoomNumber
- dpv_pd_owl:RoomNumber
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:RoomNumber

```
</details></div>