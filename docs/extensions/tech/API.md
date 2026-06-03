---
search:
  boost: 10.0
---

# Class: API 


_A set of rules and protocols to communicate and exchange data between_

_applications_



<div data-search-exclude markdown="1">



URI: [tech:API](https://w3id.org/lmodel/dpv/tech/API)





```mermaid
 classDiagram
    class API
    click API href "../API/"
      Algorithm <|-- API
        click Algorithm href "../Algorithm/"
      
      
```





## Inheritance
* [Algorithm](Algorithm.md)
    * **API**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:API](https://w3id.org/lmodel/dpv/tech/API) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* API




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#API |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:API |
| native | tech:API |
| exact | dpv_tech:API, dpv_tech_owl:API |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: API
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#API
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A set of rules and protocols to communicate and exchange data between

  applications'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- API
exact_mappings:
- dpv_tech:API
- dpv_tech_owl:API
is_a: Algorithm
class_uri: tech:API

```
</details>

### Induced

<details>
```yaml
name: API
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#API
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A set of rules and protocols to communicate and exchange data between

  applications'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- API
exact_mappings:
- dpv_tech:API
- dpv_tech_owl:API
is_a: Algorithm
class_uri: tech:API

```
</details></div>