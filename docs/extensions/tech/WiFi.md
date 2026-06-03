---
search:
  boost: 10.0
---

# Class: WiFi 


_Technology utilising Wi-Fi wireless networking_



<div data-search-exclude markdown="1">



URI: [tech:WiFi](https://w3id.org/lmodel/dpv/tech/WiFi)





```mermaid
 classDiagram
    class WiFi
    click WiFi href "../WiFi/"
      CommunicationMechanism <|-- WiFi
        click CommunicationMechanism href "../CommunicationMechanism/"
      Networking <|-- WiFi
        click Networking href "../Networking/"
      
      
```





## Inheritance
* [CommunicationMechanism](CommunicationMechanism.md)
    * [Networking](Networking.md)
        * **WiFi** [ [CommunicationMechanism](CommunicationMechanism.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:WiFi](https://w3id.org/lmodel/dpv/tech/WiFi) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* WiFi




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#WiFi |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:WiFi |
| native | tech:WiFi |
| exact | dpv_tech:WiFi, dpv_tech_owl:WiFi |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WiFi
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#WiFi
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising Wi-Fi wireless networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- WiFi
exact_mappings:
- dpv_tech:WiFi
- dpv_tech_owl:WiFi
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:WiFi

```
</details>

### Induced

<details>
```yaml
name: WiFi
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#WiFi
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising Wi-Fi wireless networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- WiFi
exact_mappings:
- dpv_tech:WiFi
- dpv_tech_owl:WiFi
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:WiFi

```
</details></div>