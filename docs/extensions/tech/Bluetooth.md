---
search:
  boost: 10.0
---

# Class: Bluetooth 


_Technology utilising bluetooth_



<div data-search-exclude markdown="1">



URI: [tech:Bluetooth](https://w3id.org/lmodel/dpv/tech/Bluetooth)





```mermaid
 classDiagram
    class Bluetooth
    click Bluetooth href "../Bluetooth/"
      CommunicationMechanism <|-- Bluetooth
        click CommunicationMechanism href "../CommunicationMechanism/"
      Networking <|-- Bluetooth
        click Networking href "../Networking/"
      
      
```





## Inheritance
* [CommunicationMechanism](CommunicationMechanism.md)
    * [Networking](Networking.md)
        * **Bluetooth** [ [CommunicationMechanism](CommunicationMechanism.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Bluetooth](https://w3id.org/lmodel/dpv/tech/Bluetooth) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Bluetooth




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Bluetooth |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Bluetooth |
| native | tech:Bluetooth |
| exact | dpv_tech:Bluetooth, dpv_tech_owl:Bluetooth |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bluetooth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Bluetooth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising bluetooth
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Bluetooth
exact_mappings:
- dpv_tech:Bluetooth
- dpv_tech_owl:Bluetooth
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:Bluetooth

```
</details>

### Induced

<details>
```yaml
name: Bluetooth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Bluetooth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising bluetooth
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Bluetooth
exact_mappings:
- dpv_tech:Bluetooth
- dpv_tech_owl:Bluetooth
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:Bluetooth

```
</details></div>