---
search:
  boost: 10.0
---

# Class: GPS 


_Technology utilising GPS_



<div data-search-exclude markdown="1">



URI: [tech:GPS](https://w3id.org/lmodel/dpv/tech/GPS)





```mermaid
 classDiagram
    class GPS
    click GPS href "../GPS/"
      CommunicationMechanism <|-- GPS
        click CommunicationMechanism href "../CommunicationMechanism/"
      
      
```





## Inheritance
* [CommunicationMechanism](CommunicationMechanism.md)
    * **GPS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:GPS](https://w3id.org/lmodel/dpv/tech/GPS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* GPS


## Comments

* This concept models GPS as a networking technology. For representing use
of GPS to get current location, see pd:GPSCoordinate and
pd:CurrentLocation concepts in PD extension



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#GPS |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:GPS |
| native | tech:GPS |
| exact | dpv_tech:GPS, dpv_tech_owl:GPS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GPS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#GPS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising GPS
comments:
- 'This concept models GPS as a networking technology. For representing use

  of GPS to get current location, see pd:GPSCoordinate and

  pd:CurrentLocation concepts in PD extension'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- GPS
exact_mappings:
- dpv_tech:GPS
- dpv_tech_owl:GPS
is_a: CommunicationMechanism
class_uri: tech:GPS

```
</details>

### Induced

<details>
```yaml
name: GPS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#GPS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising GPS
comments:
- 'This concept models GPS as a networking technology. For representing use

  of GPS to get current location, see pd:GPSCoordinate and

  pd:CurrentLocation concepts in PD extension'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- GPS
exact_mappings:
- dpv_tech:GPS
- dpv_tech_owl:GPS
is_a: CommunicationMechanism
class_uri: tech:GPS

```
</details></div>