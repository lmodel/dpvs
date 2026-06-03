---
search:
  boost: 10.0
---

# Class: Specification 


_Documentation that specifies requirements that must be satisfied by the_

_technology_



<div data-search-exclude markdown="1">



URI: [tech:Specification](https://w3id.org/lmodel/dpv/tech/Specification)





```mermaid
 classDiagram
    class Specification
    click Specification href "../Specification/"
      Documentation <|-- Specification
        click Documentation href "../Documentation/"
      
      
```





## Inheritance
* [Documentation](Documentation.md)
    * **Specification**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Specification](https://w3id.org/lmodel/dpv/tech/Specification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Specification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Specification |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Specification |
| native | tech:Specification |
| exact | dpv_tech:Specification, dpv_tech_owl:Specification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Specification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Specification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Documentation that specifies requirements that must be satisfied by
  the

  technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Specification
exact_mappings:
- dpv_tech:Specification
- dpv_tech_owl:Specification
is_a: Documentation
class_uri: tech:Specification

```
</details>

### Induced

<details>
```yaml
name: Specification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Specification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Documentation that specifies requirements that must be satisfied by
  the

  technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Specification
exact_mappings:
- dpv_tech:Specification
- dpv_tech_owl:Specification
is_a: Documentation
class_uri: tech:Specification

```
</details></div>