---
search:
  boost: 10.0
---

# Class: Recommendation 


_A recommendation or suggestion of an action or decision or choice in the_

_context of technologies_



<div data-search-exclude markdown="1">



URI: [tech:Recommendation](https://w3id.org/lmodel/dpv/tech/Recommendation)





```mermaid
 classDiagram
    class Recommendation
    click Recommendation href "../Recommendation/"
      InputOutput <|-- Recommendation
        click InputOutput href "../InputOutput/"
      
      
```





## Inheritance
* [InputOutput](InputOutput.md)
    * **Recommendation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Recommendation](https://w3id.org/lmodel/dpv/tech/Recommendation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Recommendation


## Comments

* Recommendation is a concept referring to activities or tasks in the
context of technologies producing or using them as inputs or outputs



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Recommendation |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Recommendation |
| native | tech:Recommendation |
| exact | dpv_tech:Recommendation, dpv_tech_owl:Recommendation |
| close | iso22989:Recommendation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Recommendation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Recommendation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A recommendation or suggestion of an action or decision or choice in
  the

  context of technologies'
comments:
- 'Recommendation is a concept referring to activities or tasks in the

  context of technologies producing or using them as inputs or outputs'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Recommendation
exact_mappings:
- dpv_tech:Recommendation
- dpv_tech_owl:Recommendation
close_mappings:
- iso22989:Recommendation
is_a: InputOutput
class_uri: tech:Recommendation

```
</details>

### Induced

<details>
```yaml
name: Recommendation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Recommendation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A recommendation or suggestion of an action or decision or choice in
  the

  context of technologies'
comments:
- 'Recommendation is a concept referring to activities or tasks in the

  context of technologies producing or using them as inputs or outputs'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Recommendation
exact_mappings:
- dpv_tech:Recommendation
- dpv_tech_owl:Recommendation
close_mappings:
- iso22989:Recommendation
is_a: InputOutput
class_uri: tech:Recommendation

```
</details></div>