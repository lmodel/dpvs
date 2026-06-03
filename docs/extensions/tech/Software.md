---
search:
  boost: 10.0
---

# Class: Software 


_Virtual parts or components of the technology such as programs and data_



<div data-search-exclude markdown="1">



URI: [tech:Software](https://w3id.org/lmodel/dpv/tech/Software)





```mermaid
 classDiagram
    class Software
    click Software href "../Software/"
      Software <|-- DataStorage
        click DataStorage href "../DataStorage/"
      Software <|-- DpvApplication
        click DpvApplication href "../DpvApplication/"
      Software <|-- OS
        click OS href "../OS/"
      Software <|-- SoftwareAgent
        click SoftwareAgent href "../SoftwareAgent/"
      Software <|-- SoftwareFramework
        click SoftwareFramework href "../SoftwareFramework/"
      Software <|-- SoftwareLibrary
        click SoftwareLibrary href "../SoftwareLibrary/"
      Software <|-- WebScraper
        click WebScraper href "../WebScraper/"
      
      
```





## Inheritance
* **Software**
    * [OS](OS.md)
    * [SoftwareFramework](SoftwareFramework.md)
    * [SoftwareLibrary](SoftwareLibrary.md)
    * [WebScraper](WebScraper.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Software](https://w3id.org/lmodel/dpv/tech/Software) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Software




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Software |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Software |
| native | tech:Software |
| exact | dpv_tech:Software, dpv_tech_owl:Software |
| related | iso22989:AISystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Software
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Software
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Virtual parts or components of the technology such as programs and data
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Software
exact_mappings:
- dpv_tech:Software
- dpv_tech_owl:Software
related_mappings:
- iso22989:AISystem
class_uri: tech:Software

```
</details>

### Induced

<details>
```yaml
name: Software
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Software
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Virtual parts or components of the technology such as programs and data
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Software
exact_mappings:
- dpv_tech:Software
- dpv_tech_owl:Software
related_mappings:
- iso22989:AISystem
class_uri: tech:Software

```
</details></div>