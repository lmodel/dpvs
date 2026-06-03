---
search:
  boost: 10.0
---

# Class: SoftwareLibrary 


_A collection of pre-built and reusable functions for use in development_

_and management of software_



<div data-search-exclude markdown="1">



URI: [tech:SoftwareLibrary](https://w3id.org/lmodel/dpv/tech/SoftwareLibrary)





```mermaid
 classDiagram
    class SoftwareLibrary
    click SoftwareLibrary href "../SoftwareLibrary/"
      Software <|-- SoftwareLibrary
        click Software href "../Software/"
      
      
```





## Inheritance
* [Software](Software.md)
    * **SoftwareLibrary**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:SoftwareLibrary](https://w3id.org/lmodel/dpv/tech/SoftwareLibrary) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* SoftwareLibrary




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#SoftwareLibrary |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:SoftwareLibrary |
| native | tech:SoftwareLibrary |
| exact | dpv_tech:SoftwareLibrary, dpv_tech_owl:SoftwareLibrary |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SoftwareLibrary
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SoftwareLibrary
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A collection of pre-built and reusable functions for use in development

  and management of software'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- SoftwareLibrary
exact_mappings:
- dpv_tech:SoftwareLibrary
- dpv_tech_owl:SoftwareLibrary
is_a: Software
class_uri: tech:SoftwareLibrary

```
</details>

### Induced

<details>
```yaml
name: SoftwareLibrary
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SoftwareLibrary
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A collection of pre-built and reusable functions for use in development

  and management of software'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- SoftwareLibrary
exact_mappings:
- dpv_tech:SoftwareLibrary
- dpv_tech_owl:SoftwareLibrary
is_a: Software
class_uri: tech:SoftwareLibrary

```
</details></div>