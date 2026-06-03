---
search:
  boost: 10.0
---

# Class: Internet 


_Technology utilising internet_



<div data-search-exclude markdown="1">



URI: [tech:Internet](https://w3id.org/lmodel/dpv/tech/Internet)





```mermaid
 classDiagram
    class Internet
    click Internet href "../Internet/"
      CommunicationMechanism <|-- Internet
        click CommunicationMechanism href "../CommunicationMechanism/"
      Networking <|-- Internet
        click Networking href "../Networking/"
      
      
```





## Inheritance
* [CommunicationMechanism](CommunicationMechanism.md)
    * [Networking](Networking.md)
        * **Internet** [ [CommunicationMechanism](CommunicationMechanism.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Internet](https://w3id.org/lmodel/dpv/tech/Internet) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Internet




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Internet |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Internet |
| native | tech:Internet |
| exact | dpv_tech:Internet, dpv_tech_owl:Internet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Internet
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Internet
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising internet
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Internet
exact_mappings:
- dpv_tech:Internet
- dpv_tech_owl:Internet
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:Internet

```
</details>

### Induced

<details>
```yaml
name: Internet
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Internet
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology utilising internet
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Internet
exact_mappings:
- dpv_tech:Internet
- dpv_tech_owl:Internet
is_a: Networking
mixins:
- CommunicationMechanism
class_uri: tech:Internet

```
</details></div>