---
search:
  boost: 10.0
---

# Class: Android 


_Android operating system_



<div data-search-exclude markdown="1">



URI: [tech:Android](https://w3id.org/lmodel/dpv/tech/Android)





```mermaid
 classDiagram
    class Android
    click Android href "../Android/"
      OS <|-- Android
        click OS href "../OS/"
      
      
```





## Inheritance
* [Software](Software.md)
    * [OS](OS.md)
        * **Android**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Android](https://w3id.org/lmodel/dpv/tech/Android) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Android




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Android |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Android |
| native | tech:Android |
| exact | dpv_tech:Android, dpv_tech_owl:Android |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Android
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Android
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Android operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Android
exact_mappings:
- dpv_tech:Android
- dpv_tech_owl:Android
is_a: OS
class_uri: tech:Android

```
</details>

### Induced

<details>
```yaml
name: Android
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Android
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Android operating system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Android
exact_mappings:
- dpv_tech:Android
- dpv_tech_owl:Android
is_a: OS
class_uri: tech:Android

```
</details></div>