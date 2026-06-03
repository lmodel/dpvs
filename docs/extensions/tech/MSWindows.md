---
search:
  boost: 10.0
---

# Class: MSWindows 


_Microsoft Windows operating system_



<div data-search-exclude markdown="1">



URI: [tech:MSWindows](https://w3id.org/lmodel/dpv/tech/MSWindows)





```mermaid
 classDiagram
    class MSWindows
    click MSWindows href "../MSWindows/"
      OS <|-- MSWindows
        click OS href "../OS/"
      
      
```





## Inheritance
* [Software](Software.md)
    * [OS](OS.md)
        * **MSWindows**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:MSWindows](https://w3id.org/lmodel/dpv/tech/MSWindows) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Microsoft Windows




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#MSWindows |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:MSWindows |
| native | tech:MSWindows |
| exact | dpv_tech:MSWindows, dpv_tech_owl:MSWindows |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MSWindows
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MSWindows
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Microsoft Windows operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Microsoft Windows
exact_mappings:
- dpv_tech:MSWindows
- dpv_tech_owl:MSWindows
is_a: OS
class_uri: tech:MSWindows

```
</details>

### Induced

<details>
```yaml
name: MSWindows
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MSWindows
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Microsoft Windows operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Microsoft Windows
exact_mappings:
- dpv_tech:MSWindows
- dpv_tech_owl:MSWindows
is_a: OS
class_uri: tech:MSWindows

```
</details></div>