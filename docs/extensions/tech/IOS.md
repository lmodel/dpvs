---
search:
  boost: 10.0
---

# Class: IOS 


_iOS operating system_



<div data-search-exclude markdown="1">



URI: [tech:iOS](https://w3id.org/lmodel/dpv/tech/iOS)





```mermaid
 classDiagram
    class IOS
    click IOS href "../IOS/"
      OS <|-- IOS
        click OS href "../OS/"
      
      
```





## Inheritance
* [Software](Software.md)
    * [OS](OS.md)
        * **IOS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:iOS](https://w3id.org/lmodel/dpv/tech/iOS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* iOS




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#iOS |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:iOS |
| native | tech:IOS |
| exact | dpv_tech:iOS, dpv_tech_owl:iOS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: iOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#iOS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: iOS operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- iOS
exact_mappings:
- dpv_tech:iOS
- dpv_tech_owl:iOS
is_a: OS
class_uri: tech:iOS

```
</details>

### Induced

<details>
```yaml
name: iOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#iOS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: iOS operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- iOS
exact_mappings:
- dpv_tech:iOS
- dpv_tech_owl:iOS
is_a: OS
class_uri: tech:iOS

```
</details></div>