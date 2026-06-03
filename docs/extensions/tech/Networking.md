---
search:
  boost: 10.0
---

# Class: Networking 


_Technology utilising networking_



<div data-search-exclude markdown="1">



URI: [tech:Networking](https://w3id.org/lmodel/dpv/tech/Networking)





```mermaid
 classDiagram
    class Networking
    click Networking href "../Networking/"
      CommunicationMechanism <|-- Networking
        click CommunicationMechanism href "../CommunicationMechanism/"
      

      Networking <|-- Bluetooth
        click Bluetooth href "../Bluetooth/"
      Networking <|-- CellularNetwork
        click CellularNetwork href "../CellularNetwork/"
      Networking <|-- Internet
        click Internet href "../Internet/"
      Networking <|-- LocalNetwork
        click LocalNetwork href "../LocalNetwork/"
      Networking <|-- WiFi
        click WiFi href "../WiFi/"
      

      
```





## Inheritance
* [CommunicationMechanism](CommunicationMechanism.md)
    * **Networking**
        * [Bluetooth](Bluetooth.md) [ [CommunicationMechanism](CommunicationMechanism.md)]
        * [CellularNetwork](CellularNetwork.md) [ [CommunicationMechanism](CommunicationMechanism.md)]
        * [Internet](Internet.md) [ [CommunicationMechanism](CommunicationMechanism.md)]
        * [LocalNetwork](LocalNetwork.md) [ [CommunicationMechanism](CommunicationMechanism.md)]
        * [WiFi](WiFi.md) [ [CommunicationMechanism](CommunicationMechanism.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Networking](https://w3id.org/lmodel/dpv/tech/Networking) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Networking




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Networking |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Networking |
| native | tech:Networking |
| exact | dpv_tech:Networking, dpv_tech_owl:Networking |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Networking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Networking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Networking
exact_mappings:
- dpv_tech:Networking
- dpv_tech_owl:Networking
is_a: CommunicationMechanism
class_uri: tech:Networking

```
</details>

### Induced

<details>
```yaml
name: Networking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Networking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Networking
exact_mappings:
- dpv_tech:Networking
- dpv_tech_owl:Networking
is_a: CommunicationMechanism
class_uri: tech:Networking

```
</details></div>