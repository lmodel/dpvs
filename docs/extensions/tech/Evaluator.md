---
search:
  boost: 10.0
---

# Class: Evaluator 


_Actor that evaluates the performance of Technology_



<div data-search-exclude markdown="1">



URI: [tech:Evaluator](https://w3id.org/lmodel/dpv/tech/Evaluator)





```mermaid
 classDiagram
    class Evaluator
    click Evaluator href "../Evaluator/"
      Actor <|-- Evaluator
        click Actor href "../Actor/"
      Partner <|-- Evaluator
        click Partner href "../Partner/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * [Partner](Partner.md)
        * **Evaluator** [ [Actor](Actor.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Evaluator](https://w3id.org/lmodel/dpv/tech/Evaluator) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Evaluator




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Evaluator |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Evaluator |
| native | tech:Evaluator |
| exact | dpv_tech:Evaluator, dpv_tech_owl:Evaluator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Evaluator
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Evaluator
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that evaluates the performance of Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Evaluator
exact_mappings:
- dpv_tech:Evaluator
- dpv_tech_owl:Evaluator
is_a: Partner
mixins:
- Actor
class_uri: tech:Evaluator

```
</details>

### Induced

<details>
```yaml
name: Evaluator
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Evaluator
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that evaluates the performance of Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Evaluator
exact_mappings:
- dpv_tech:Evaluator
- dpv_tech_owl:Evaluator
is_a: Partner
mixins:
- Actor
class_uri: tech:Evaluator

```
</details></div>