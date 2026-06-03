---
search:
  boost: 10.0
---

# Class: Hardware 


_Physical parts or components of the technology_



<div data-search-exclude markdown="1">



URI: [tech:Hardware](https://w3id.org/lmodel/dpv/tech/Hardware)





```mermaid
 classDiagram
    class Hardware
    click Hardware href "../Hardware/"
      Hardware <|-- Device
        click Device href "../Device/"
      Hardware <|-- IntegratedCircuit
        click IntegratedCircuit href "../IntegratedCircuit/"
      Hardware <|-- IoT
        click IoT href "../IoT/"
      
      
```





## Inheritance
* **Hardware**
    * [IntegratedCircuit](IntegratedCircuit.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Hardware](https://w3id.org/lmodel/dpv/tech/Hardware) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Hardware




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Hardware |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Hardware |
| native | tech:Hardware |
| exact | dpv_tech:Hardware, dpv_tech_owl:Hardware |
| related | iso22989:AISystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Hardware
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Hardware
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Physical parts or components of the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Hardware
exact_mappings:
- dpv_tech:Hardware
- dpv_tech_owl:Hardware
related_mappings:
- iso22989:AISystem
class_uri: tech:Hardware

```
</details>

### Induced

<details>
```yaml
name: Hardware
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Hardware
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Physical parts or components of the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Hardware
exact_mappings:
- dpv_tech:Hardware
- dpv_tech_owl:Hardware
related_mappings:
- iso22989:AISystem
class_uri: tech:Hardware

```
</details></div>