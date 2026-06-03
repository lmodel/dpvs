---
search:
  boost: 10.0
---

# Class: Developer 


_Actor that develops Technology_



<div data-search-exclude markdown="1">



URI: [tech:Developer](https://w3id.org/lmodel/dpv/tech/Developer)





```mermaid
 classDiagram
    class Developer
    click Developer href "../Developer/"
      Actor <|-- Developer
        click Actor href "../Actor/"
      DpvProducer <|-- Developer
        click DpvProducer href "../DpvProducer/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * [DpvProducer](DpvProducer.md)
        * **Developer** [ [Actor](Actor.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Developer](https://w3id.org/lmodel/dpv/tech/Developer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Developer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Developer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Developer |
| native | tech:Developer |
| exact | dpv_tech:Developer, dpv_tech_owl:Developer |
| close | iso22989:Stakeholder |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Developer
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Developer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that develops Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Developer
exact_mappings:
- dpv_tech:Developer
- dpv_tech_owl:Developer
close_mappings:
- iso22989:Stakeholder
is_a: DpvProducer
mixins:
- Actor
class_uri: tech:Developer

```
</details>

### Induced

<details>
```yaml
name: Developer
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Developer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that develops Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Developer
exact_mappings:
- dpv_tech:Developer
- dpv_tech_owl:Developer
close_mappings:
- iso22989:Stakeholder
is_a: DpvProducer
mixins:
- Actor
class_uri: tech:Developer

```
</details></div>