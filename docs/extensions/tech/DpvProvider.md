---
search:
  boost: 10.0
---

# Class: DpvProvider 


_Actor that provides Technology_



<div data-search-exclude markdown="1">



URI: [tech:Provider](https://w3id.org/lmodel/dpv/tech/Provider)





```mermaid
 classDiagram
    class DpvProvider
    click DpvProvider href "../DpvProvider/"
      Actor <|-- DpvProvider
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **DpvProvider**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Provider](https://w3id.org/lmodel/dpv/tech/Provider) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provider




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Provider |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Provider |
| native | tech:DpvProvider |
| exact | dpv_tech:Provider, dpv_tech_owl:Provider |
| close | iso22989:Stakeholder |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvProvider
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Provider
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that provides Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provider
exact_mappings:
- dpv_tech:Provider
- dpv_tech_owl:Provider
close_mappings:
- iso22989:Stakeholder
is_a: Actor
class_uri: tech:Provider

```
</details>

### Induced

<details>
```yaml
name: DpvProvider
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Provider
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that provides Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provider
exact_mappings:
- dpv_tech:Provider
- dpv_tech_owl:Provider
close_mappings:
- iso22989:Stakeholder
is_a: Actor
class_uri: tech:Provider

```
</details></div>