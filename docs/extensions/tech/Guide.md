---
search:
  boost: 10.0
---

# Class: Guide 


_Documentation that provides guidance regarding the technology_



<div data-search-exclude markdown="1">



URI: [tech:Guide](https://w3id.org/lmodel/dpv/tech/Guide)





```mermaid
 classDiagram
    class Guide
    click Guide href "../Guide/"
      Documentation <|-- Guide
        click Documentation href "../Documentation/"
      
      
```





## Inheritance
* [Documentation](Documentation.md)
    * **Guide**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Guide](https://w3id.org/lmodel/dpv/tech/Guide) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Guide




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Guide |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Guide |
| native | tech:Guide |
| exact | dpv_tech:Guide, dpv_tech_owl:Guide |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Guide
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Guide
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Documentation that provides guidance regarding the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Guide
exact_mappings:
- dpv_tech:Guide
- dpv_tech_owl:Guide
is_a: Documentation
class_uri: tech:Guide

```
</details>

### Induced

<details>
```yaml
name: Guide
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Guide
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Documentation that provides guidance regarding the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Guide
exact_mappings:
- dpv_tech:Guide
- dpv_tech_owl:Guide
is_a: Documentation
class_uri: tech:Guide

```
</details></div>