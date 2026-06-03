---
search:
  boost: 10.0
---

# Class: Distributor 


_Actor that distributes the Technology_



<div data-search-exclude markdown="1">



URI: [tech:Distributor](https://w3id.org/lmodel/dpv/tech/Distributor)





```mermaid
 classDiagram
    class Distributor
    click Distributor href "../Distributor/"
      Actor <|-- Distributor
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Distributor**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Distributor](https://w3id.org/lmodel/dpv/tech/Distributor) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Distributor




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Distributor |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Distributor |
| native | tech:Distributor |
| exact | dpv_tech:Distributor, dpv_tech_owl:Distributor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Distributor
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Distributor
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that distributes the Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Distributor
exact_mappings:
- dpv_tech:Distributor
- dpv_tech_owl:Distributor
is_a: Actor
class_uri: tech:Distributor

```
</details>

### Induced

<details>
```yaml
name: Distributor
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Distributor
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that distributes the Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Distributor
exact_mappings:
- dpv_tech:Distributor
- dpv_tech_owl:Distributor
is_a: Actor
class_uri: tech:Distributor

```
</details></div>