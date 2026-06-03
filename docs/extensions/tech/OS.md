---
search:
  boost: 10.0
---

# Class: OS 


_Software for managing hardware and other software_



<div data-search-exclude markdown="1">



URI: [tech:OS](https://w3id.org/lmodel/dpv/tech/OS)





```mermaid
 classDiagram
    class OS
    click OS href "../OS/"
      Software <|-- OS
        click Software href "../Software/"
      

      OS <|-- Android
        click Android href "../Android/"
      OS <|-- GNULinux
        click GNULinux href "../GNULinux/"
      OS <|-- MSWindows
        click MSWindows href "../MSWindows/"
      OS <|-- IOS
        click IOS href "../IOS/"
      

      
```





## Inheritance
* [Software](Software.md)
    * **OS**
        * [Android](Android.md)
        * [GNULinux](GNULinux.md)
        * [MSWindows](MSWindows.md)
        * [IOS](IOS.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:OS](https://w3id.org/lmodel/dpv/tech/OS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Operating System (OS)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#OS |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:OS |
| native | tech:OS |
| exact | dpv_tech:OS, dpv_tech_owl:OS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#OS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Software for managing hardware and other software
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Operating System (OS)
exact_mappings:
- dpv_tech:OS
- dpv_tech_owl:OS
is_a: Software
class_uri: tech:OS

```
</details>

### Induced

<details>
```yaml
name: OS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#OS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Software for managing hardware and other software
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Operating System (OS)
exact_mappings:
- dpv_tech:OS
- dpv_tech_owl:OS
is_a: Software
class_uri: tech:OS

```
</details></div>