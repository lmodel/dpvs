---
search:
  boost: 10.0
---

# Class: DpvSubject 


_Actor that is subjected to the use or impact of Technology_



<div data-search-exclude markdown="1">



URI: [tech:Subject](https://w3id.org/lmodel/dpv/tech/Subject)





```mermaid
 classDiagram
    class DpvSubject
    click DpvSubject href "../DpvSubject/"
      Actor <|-- DpvSubject
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **DpvSubject**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Subject](https://w3id.org/lmodel/dpv/tech/Subject) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Subject


## Comments

* Subject can be a human or non-human entity. To explicitly indicate that
the subject is a human, and to reuse DPV's human subject taxonomy, the
tech:Subject should also be defined as an instance or category of
dpv:HumanSubject



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Subject |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Subject |
| native | tech:DpvSubject |
| exact | dpv_tech:Subject, dpv_tech_owl:Subject |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvSubject
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Subject
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that is subjected to the use or impact of Technology
comments:
- 'Subject can be a human or non-human entity. To explicitly indicate that

  the subject is a human, and to reuse DPV''s human subject taxonomy, the

  tech:Subject should also be defined as an instance or category of

  dpv:HumanSubject'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Subject
exact_mappings:
- dpv_tech:Subject
- dpv_tech_owl:Subject
is_a: Actor
class_uri: tech:Subject

```
</details>

### Induced

<details>
```yaml
name: DpvSubject
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Subject
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that is subjected to the use or impact of Technology
comments:
- 'Subject can be a human or non-human entity. To explicitly indicate that

  the subject is a human, and to reuse DPV''s human subject taxonomy, the

  tech:Subject should also be defined as an instance or category of

  dpv:HumanSubject'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Subject
exact_mappings:
- dpv_tech:Subject
- dpv_tech_owl:Subject
is_a: Actor
class_uri: tech:Subject

```
</details></div>