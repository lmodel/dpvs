---
search:
  boost: 10.0
---

# Class: Owner 


_Actor that owns Technology_



<div data-search-exclude markdown="1">



URI: [tech:Owner](https://w3id.org/lmodel/dpv/tech/Owner)





```mermaid
 classDiagram
    class Owner
    click Owner href "../Owner/"
      Actor <|-- Owner
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Owner**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Owner](https://w3id.org/lmodel/dpv/tech/Owner) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Owner




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | DGA 26.3 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Owner |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Owner |
| native | tech:Owner |
| exact | dpv_tech:Owner, dpv_tech_owl:Owner |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Owner
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Owner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that owns Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Owner
exact_mappings:
- dpv_tech:Owner
- dpv_tech_owl:Owner
is_a: Actor
class_uri: tech:Owner

```
</details>

### Induced

<details>
```yaml
name: Owner
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Owner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that owns Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Owner
exact_mappings:
- dpv_tech:Owner
- dpv_tech_owl:Owner
is_a: Actor
class_uri: tech:Owner

```
</details></div>