---
search:
  boost: 10.0
---

# Class: SoftwareFramework 


_An opinionated collection of functions and architecture design choices_

_for building applications_



<div data-search-exclude markdown="1">



URI: [tech:SoftwareFramework](https://w3id.org/lmodel/dpv/tech/SoftwareFramework)





```mermaid
 classDiagram
    class SoftwareFramework
    click SoftwareFramework href "../SoftwareFramework/"
      Software <|-- SoftwareFramework
        click Software href "../Software/"
      
      
```





## Inheritance
* [Software](Software.md)
    * **SoftwareFramework**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:SoftwareFramework](https://w3id.org/lmodel/dpv/tech/SoftwareFramework) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* SoftwareFramework




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#SoftwareFramework |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:SoftwareFramework |
| native | tech:SoftwareFramework |
| exact | dpv_tech:SoftwareFramework, dpv_tech_owl:SoftwareFramework |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SoftwareFramework
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SoftwareFramework
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'An opinionated collection of functions and architecture design choices

  for building applications'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- SoftwareFramework
exact_mappings:
- dpv_tech:SoftwareFramework
- dpv_tech_owl:SoftwareFramework
is_a: Software
class_uri: tech:SoftwareFramework

```
</details>

### Induced

<details>
```yaml
name: SoftwareFramework
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SoftwareFramework
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'An opinionated collection of functions and architecture design choices

  for building applications'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- SoftwareFramework
exact_mappings:
- dpv_tech:SoftwareFramework
- dpv_tech_owl:SoftwareFramework
is_a: Software
class_uri: tech:SoftwareFramework

```
</details></div>