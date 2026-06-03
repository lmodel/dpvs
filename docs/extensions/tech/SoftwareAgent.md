---
search:
  boost: 10.0
---

# Class: SoftwareAgent 


_A software that acts on behalf of another Entity or technology_



<div data-search-exclude markdown="1">



URI: [tech:SoftwareAgent](https://w3id.org/lmodel/dpv/tech/SoftwareAgent)





```mermaid
 classDiagram
    class SoftwareAgent
    click SoftwareAgent href "../SoftwareAgent/"
      Software <|-- SoftwareAgent
        click Software href "../Software/"
      

      SoftwareAgent <|-- UserAgent
        click UserAgent href "../UserAgent/"
      

      
```





## Inheritance
* **SoftwareAgent** [ [Software](Software.md)]
    * [UserAgent](UserAgent.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:SoftwareAgent](https://w3id.org/lmodel/dpv/tech/SoftwareAgent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Software Agent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#SoftwareAgent |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:SoftwareAgent |
| native | tech:SoftwareAgent |
| exact | dpv_tech:SoftwareAgent, dpv_tech_owl:SoftwareAgent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SoftwareAgent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SoftwareAgent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A software that acts on behalf of another Entity or technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Software Agent
exact_mappings:
- dpv_tech:SoftwareAgent
- dpv_tech_owl:SoftwareAgent
mixins:
- Software
class_uri: tech:SoftwareAgent

```
</details>

### Induced

<details>
```yaml
name: SoftwareAgent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SoftwareAgent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A software that acts on behalf of another Entity or technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Software Agent
exact_mappings:
- dpv_tech:SoftwareAgent
- dpv_tech_owl:SoftwareAgent
mixins:
- Software
class_uri: tech:SoftwareAgent

```
</details></div>