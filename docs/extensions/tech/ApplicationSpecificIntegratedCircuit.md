---
search:
  boost: 10.0
---

# Class: ApplicationSpecificIntegratedCircuit 


_A custom-designed integrated circuit optimised for a specific task_



<div data-search-exclude markdown="1">



URI: [tech:ApplicationSpecificIntegratedCircuit](https://w3id.org/lmodel/dpv/tech/ApplicationSpecificIntegratedCircuit)





```mermaid
 classDiagram
    class ApplicationSpecificIntegratedCircuit
    click ApplicationSpecificIntegratedCircuit href "../ApplicationSpecificIntegratedCircuit/"
      IntegratedCircuit <|-- ApplicationSpecificIntegratedCircuit
        click IntegratedCircuit href "../IntegratedCircuit/"
      
      
```





## Inheritance
* [Hardware](Hardware.md)
    * [IntegratedCircuit](IntegratedCircuit.md)
        * **ApplicationSpecificIntegratedCircuit**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ApplicationSpecificIntegratedCircuit](https://w3id.org/lmodel/dpv/tech/ApplicationSpecificIntegratedCircuit) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* ApplicationSpecificIntegratedCircuit




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ApplicationSpecificIntegratedCircuit |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ApplicationSpecificIntegratedCircuit |
| native | tech:ApplicationSpecificIntegratedCircuit |
| exact | dpv_tech:ApplicationSpecificIntegratedCircuit, dpv_tech_owl:ApplicationSpecificIntegratedCircuit |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ApplicationSpecificIntegratedCircuit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ApplicationSpecificIntegratedCircuit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A custom-designed integrated circuit optimised for a specific task
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- ApplicationSpecificIntegratedCircuit
exact_mappings:
- dpv_tech:ApplicationSpecificIntegratedCircuit
- dpv_tech_owl:ApplicationSpecificIntegratedCircuit
is_a: IntegratedCircuit
class_uri: tech:ApplicationSpecificIntegratedCircuit

```
</details>

### Induced

<details>
```yaml
name: ApplicationSpecificIntegratedCircuit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ApplicationSpecificIntegratedCircuit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A custom-designed integrated circuit optimised for a specific task
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- ApplicationSpecificIntegratedCircuit
exact_mappings:
- dpv_tech:ApplicationSpecificIntegratedCircuit
- dpv_tech_owl:ApplicationSpecificIntegratedCircuit
is_a: IntegratedCircuit
class_uri: tech:ApplicationSpecificIntegratedCircuit

```
</details></div>