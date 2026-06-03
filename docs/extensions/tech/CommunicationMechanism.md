---
search:
  boost: 10.0
---

# Class: CommunicationMechanism 


_Communication mechanism used or provided by Technology_



<div data-search-exclude markdown="1">



URI: [tech:CommunicationMechanism](https://w3id.org/lmodel/dpv/tech/CommunicationMechanism)





```mermaid
 classDiagram
    class CommunicationMechanism
    click CommunicationMechanism href "../CommunicationMechanism/"
      CommunicationMechanism <|-- Bluetooth
        click Bluetooth href "../Bluetooth/"
      CommunicationMechanism <|-- CellularNetwork
        click CellularNetwork href "../CellularNetwork/"
      CommunicationMechanism <|-- GPS
        click GPS href "../GPS/"
      CommunicationMechanism <|-- Internet
        click Internet href "../Internet/"
      CommunicationMechanism <|-- LocalNetwork
        click LocalNetwork href "../LocalNetwork/"
      CommunicationMechanism <|-- Networking
        click Networking href "../Networking/"
      CommunicationMechanism <|-- WiFi
        click WiFi href "../WiFi/"
      
      
```





## Inheritance
* **CommunicationMechanism**
    * [GPS](GPS.md)
    * [Networking](Networking.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:CommunicationMechanism](https://w3id.org/lmodel/dpv/tech/CommunicationMechanism) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Communication Mechanism




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#CommunicationMechanism |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:CommunicationMechanism |
| native | tech:CommunicationMechanism |
| exact | dpv_tech:CommunicationMechanism, dpv_tech_owl:CommunicationMechanism |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CommunicationMechanism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#CommunicationMechanism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Communication mechanism used or provided by Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Communication Mechanism
exact_mappings:
- dpv_tech:CommunicationMechanism
- dpv_tech_owl:CommunicationMechanism
class_uri: tech:CommunicationMechanism

```
</details>

### Induced

<details>
```yaml
name: CommunicationMechanism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#CommunicationMechanism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Communication mechanism used or provided by Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Communication Mechanism
exact_mappings:
- dpv_tech:CommunicationMechanism
- dpv_tech_owl:CommunicationMechanism
class_uri: tech:CommunicationMechanism

```
</details></div>