---
search:
  boost: 10.0
---

# Class: GNULinux 


_GNU/Linux operating system_



<div data-search-exclude markdown="1">



URI: [tech:GNULinux](https://w3id.org/lmodel/dpv/tech/GNULinux)





```mermaid
 classDiagram
    class GNULinux
    click GNULinux href "../GNULinux/"
      OS <|-- GNULinux
        click OS href "../OS/"
      
      
```





## Inheritance
* [Software](Software.md)
    * [OS](OS.md)
        * **GNULinux**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:GNULinux](https://w3id.org/lmodel/dpv/tech/GNULinux) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* GNU/Linux




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#GNULinux |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:GNULinux |
| native | tech:GNULinux |
| exact | dpv_tech:GNULinux, dpv_tech_owl:GNULinux |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GNULinux
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#GNULinux
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: GNU/Linux operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- GNU/Linux
exact_mappings:
- dpv_tech:GNULinux
- dpv_tech_owl:GNULinux
is_a: OS
class_uri: tech:GNULinux

```
</details>

### Induced

<details>
```yaml
name: GNULinux
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#GNULinux
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: GNU/Linux operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- GNU/Linux
exact_mappings:
- dpv_tech:GNULinux
- dpv_tech_owl:GNULinux
is_a: OS
class_uri: tech:GNULinux

```
</details></div>