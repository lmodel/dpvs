---
search:
  boost: 10.0
---

# Class: LocalNetwork 


_Technology utilising local networking_



<div data-search-exclude markdown="1">



URI: [tech:LocalNetwork](https://w3id.org/lmodel/dpv/tech/LocalNetwork)





```mermaid
 classDiagram
    class LocalNetwork
    click LocalNetwork href "../LocalNetwork/"
      CommunicationMechanism <|-- LocalNetwork
        click CommunicationMechanism href "../CommunicationMechanism/"
      Networking <|-- LocalNetwork
        click Networking href "../Networking/"
      
      
```





## Inheritance
* [CommunicationMechanism](CommunicationMechanism.md)
    * [Networking](Networking.md)
        * **LocalNetwork** [ [CommunicationMechanism](CommunicationMechanism.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:LocalNetwork](https://w3id.org/lmodel/dpv/tech/LocalNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Local Network




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#LocalNetwork |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:LocalNetwork |
| native | tech:LocalNetwork |
| exact | dpv_tech:LocalNetwork, dpv_tech_owl:LocalNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LocalNetwork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#LocalNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising local networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Local Network
exact_mappings:
- dpv_tech:LocalNetwork
- dpv_tech_owl:LocalNetwork
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:LocalNetwork

```
</details>

### Induced

<details>
```yaml
name: LocalNetwork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#LocalNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising local networking
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Local Network
exact_mappings:
- dpv_tech:LocalNetwork
- dpv_tech_owl:LocalNetwork
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:LocalNetwork

```
</details></div>