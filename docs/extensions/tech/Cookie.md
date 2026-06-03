---
search:
  boost: 10.0
---

# Class: Cookie 


_A HTTP or web or internet cookie_



<div data-search-exclude markdown="1">



URI: [tech:Cookie](https://w3id.org/lmodel/dpv/tech/Cookie)





```mermaid
 classDiagram
    class Cookie
    click Cookie href "../Cookie/"
      LocalStorage <|-- Cookie
        click LocalStorage href "../LocalStorage/"
      
      
```





## Inheritance
* **Cookie** [ [LocalStorage](LocalStorage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Cookie](https://w3id.org/lmodel/dpv/tech/Cookie) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Cookie




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Cookie |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Cookie |
| native | tech:Cookie |
| exact | dpv_tech:Cookie, dpv_tech_owl:Cookie |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Cookie
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Cookie
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A HTTP or web or internet cookie
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Cookie
exact_mappings:
- dpv_tech:Cookie
- dpv_tech_owl:Cookie
mixins:
- LocalStorage
class_uri: tech:Cookie

```
</details>

### Induced

<details>
```yaml
name: Cookie
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Cookie
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A HTTP or web or internet cookie
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Cookie
exact_mappings:
- dpv_tech:Cookie
- dpv_tech_owl:Cookie
mixins:
- LocalStorage
class_uri: tech:Cookie

```
</details></div>