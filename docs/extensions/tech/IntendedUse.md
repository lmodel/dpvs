---
search:
  boost: 10.0
---

# Class: IntendedUse 


_Describes the 'intended' use of the technology_



<div data-search-exclude markdown="1">



URI: [tech:IntendedUse](https://w3id.org/lmodel/dpv/tech/IntendedUse)





```mermaid
 classDiagram
    class IntendedUse
    click IntendedUse href "../IntendedUse/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:IntendedUse](https://w3id.org/lmodel/dpv/tech/IntendedUse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Intended Use


## Comments

* Intended use can be used to describe how the developer or provider of
technology intends it to be used e.g. use a database to store data, and
to describe the plan or 'intent' to use the technology by a user or
operator e.g. use a database to store and analyse data. Intended Use can
involve any concept e.g. DPV's purpose, processing, tech/org measures,
and can be low-level purely technical uses such as store data or
high-level goals such as legal compliance. Intended Use only describes
the intent or ex-ante intention, and may be different from how the
technology is being actually used - which is indicated by using
isImplementedUsingTechnology in a process or other relevant context.



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#IntendedUse |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:IntendedUse |
| native | tech:IntendedUse |
| exact | dpv_tech:IntendedUse, dpv_tech_owl:IntendedUse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntendedUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#IntendedUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Describes the 'intended' use of the technology
comments:
- 'Intended use can be used to describe how the developer or provider of

  technology intends it to be used e.g. use a database to store data, and

  to describe the plan or ''intent'' to use the technology by a user or

  operator e.g. use a database to store and analyse data. Intended Use can

  involve any concept e.g. DPV''s purpose, processing, tech/org measures,

  and can be low-level purely technical uses such as store data or

  high-level goals such as legal compliance. Intended Use only describes

  the intent or ex-ante intention, and may be different from how the

  technology is being actually used - which is indicated by using

  isImplementedUsingTechnology in a process or other relevant context.'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Intended Use
exact_mappings:
- dpv_tech:IntendedUse
- dpv_tech_owl:IntendedUse
class_uri: tech:IntendedUse

```
</details>

### Induced

<details>
```yaml
name: IntendedUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#IntendedUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Describes the 'intended' use of the technology
comments:
- 'Intended use can be used to describe how the developer or provider of

  technology intends it to be used e.g. use a database to store data, and

  to describe the plan or ''intent'' to use the technology by a user or

  operator e.g. use a database to store and analyse data. Intended Use can

  involve any concept e.g. DPV''s purpose, processing, tech/org measures,

  and can be low-level purely technical uses such as store data or

  high-level goals such as legal compliance. Intended Use only describes

  the intent or ex-ante intention, and may be different from how the

  technology is being actually used - which is indicated by using

  isImplementedUsingTechnology in a process or other relevant context.'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Intended Use
exact_mappings:
- dpv_tech:IntendedUse
- dpv_tech_owl:IntendedUse
class_uri: tech:IntendedUse

```
</details></div>