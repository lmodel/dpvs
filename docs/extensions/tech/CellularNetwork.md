---
search:
  boost: 10.0
---

# Class: CellularNetwork 


_Technology utilising cellular networking_



<div data-search-exclude markdown="1">



URI: [tech:CellularNetwork](https://w3id.org/lmodel/dpv/tech/CellularNetwork)





```mermaid
 classDiagram
    class CellularNetwork
    click CellularNetwork href "../CellularNetwork/"
      CommunicationMechanism <|-- CellularNetwork
        click CommunicationMechanism href "../CommunicationMechanism/"
      Networking <|-- CellularNetwork
        click Networking href "../Networking/"
      
      
```





## Inheritance
* [CommunicationMechanism](CommunicationMechanism.md)
    * [Networking](Networking.md)
        * **CellularNetwork** [ [CommunicationMechanism](CommunicationMechanism.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:CellularNetwork](https://w3id.org/lmodel/dpv/tech/CellularNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Cellular Network




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#CellularNetwork |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:CellularNetwork |
| native | tech:CellularNetwork |
| exact | dpv_tech:CellularNetwork, dpv_tech_owl:CellularNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellularNetwork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#CellularNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising cellular networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Cellular Network
exact_mappings:
- dpv_tech:CellularNetwork
- dpv_tech_owl:CellularNetwork
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:CellularNetwork

```
</details>

### Induced

<details>
```yaml
name: CellularNetwork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#CellularNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising cellular networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Cellular Network
exact_mappings:
- dpv_tech:CellularNetwork
- dpv_tech_owl:CellularNetwork
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:CellularNetwork

```
</details></div>