---
search:
  boost: 10.0
---

# Class: IntegratedCircuit 


_A integrated electronic chip containing interconnected components to_

_perform specific functions_



<div data-search-exclude markdown="1">



URI: [tech:IntegratedCircuit](https://w3id.org/lmodel/dpv/tech/IntegratedCircuit)





```mermaid
 classDiagram
    class IntegratedCircuit
    click IntegratedCircuit href "../IntegratedCircuit/"
      Hardware <|-- IntegratedCircuit
        click Hardware href "../Hardware/"
      

      IntegratedCircuit <|-- ApplicationSpecificIntegratedCircuit
        click ApplicationSpecificIntegratedCircuit href "../ApplicationSpecificIntegratedCircuit/"
      

      
```





## Inheritance
* [Hardware](Hardware.md)
    * **IntegratedCircuit**
        * [ApplicationSpecificIntegratedCircuit](ApplicationSpecificIntegratedCircuit.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:IntegratedCircuit](https://w3id.org/lmodel/dpv/tech/IntegratedCircuit) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* IntegratedCircuit




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#IntegratedCircuit |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:IntegratedCircuit |
| native | tech:IntegratedCircuit |
| exact | dpv_tech:IntegratedCircuit, dpv_tech_owl:IntegratedCircuit |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntegratedCircuit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#IntegratedCircuit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A integrated electronic chip containing interconnected components to

  perform specific functions'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- IntegratedCircuit
exact_mappings:
- dpv_tech:IntegratedCircuit
- dpv_tech_owl:IntegratedCircuit
is_a: Hardware
class_uri: tech:IntegratedCircuit

```
</details>

### Induced

<details>
```yaml
name: IntegratedCircuit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#IntegratedCircuit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A integrated electronic chip containing interconnected components to

  perform specific functions'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- IntegratedCircuit
exact_mappings:
- dpv_tech:IntegratedCircuit
- dpv_tech_owl:IntegratedCircuit
is_a: Hardware
class_uri: tech:IntegratedCircuit

```
</details></div>