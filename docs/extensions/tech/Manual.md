---
search:
  boost: 10.0
---

# Class: Manual 


_Documentation that provides instructions for using, maintaining,_

_developing, or performing other activities regarding the technology_



<div data-search-exclude markdown="1">



URI: [tech:Manual](https://w3id.org/lmodel/dpv/tech/Manual)





```mermaid
 classDiagram
    class Manual
    click Manual href "../Manual/"
      Documentation <|-- Manual
        click Documentation href "../Documentation/"
      
      
```





## Inheritance
* [Documentation](Documentation.md)
    * **Manual**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Manual](https://w3id.org/lmodel/dpv/tech/Manual) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Manual




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Manual |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Manual |
| native | tech:Manual |
| exact | dpv_tech:Manual, dpv_tech_owl:Manual |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Manual
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Manual
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Documentation that provides instructions for using, maintaining,

  developing, or performing other activities regarding the technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Manual
exact_mappings:
- dpv_tech:Manual
- dpv_tech_owl:Manual
is_a: Documentation
class_uri: tech:Manual

```
</details>

### Induced

<details>
```yaml
name: Manual
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Manual
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Documentation that provides instructions for using, maintaining,

  developing, or performing other activities regarding the technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Manual
exact_mappings:
- dpv_tech:Manual
- dpv_tech_owl:Manual
is_a: Documentation
class_uri: tech:Manual

```
</details></div>