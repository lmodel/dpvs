---
search:
  boost: 10.0
---

# Class: SystemIntegrator 


_Actor that integrates Technology in to (larger) systems_



<div data-search-exclude markdown="1">



URI: [tech:SystemIntegrator](https://w3id.org/lmodel/dpv/tech/SystemIntegrator)





```mermaid
 classDiagram
    class SystemIntegrator
    click SystemIntegrator href "../SystemIntegrator/"
      Actor <|-- SystemIntegrator
        click Actor href "../Actor/"
      Partner <|-- SystemIntegrator
        click Partner href "../Partner/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * [Partner](Partner.md)
        * **SystemIntegrator** [ [Actor](Actor.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:SystemIntegrator](https://w3id.org/lmodel/dpv/tech/SystemIntegrator) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* System Integrator




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#SystemIntegrator |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:SystemIntegrator |
| native | tech:SystemIntegrator |
| exact | dpv_tech:SystemIntegrator, dpv_tech_owl:SystemIntegrator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SystemIntegrator
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SystemIntegrator
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that integrates Technology in to (larger) systems
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- System Integrator
exact_mappings:
- dpv_tech:SystemIntegrator
- dpv_tech_owl:SystemIntegrator
is_a: Partner
mixins:
- Actor
class_uri: tech:SystemIntegrator

```
</details>

### Induced

<details>
```yaml
name: SystemIntegrator
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SystemIntegrator
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that integrates Technology in to (larger) systems
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- System Integrator
exact_mappings:
- dpv_tech:SystemIntegrator
- dpv_tech_owl:SystemIntegrator
is_a: Partner
mixins:
- Actor
class_uri: tech:SystemIntegrator

```
</details></div>