---
search:
  boost: 10.0
---

# Class: Prediction 


_An inference or prediction of an action or data or decision in the_

_context of technologies_



<div data-search-exclude markdown="1">



URI: [tech:Prediction](https://w3id.org/lmodel/dpv/tech/Prediction)





```mermaid
 classDiagram
    class Prediction
    click Prediction href "../Prediction/"
      InputOutput <|-- Prediction
        click InputOutput href "../InputOutput/"
      
      
```





## Inheritance
* [InputOutput](InputOutput.md)
    * **Prediction**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Prediction](https://w3id.org/lmodel/dpv/tech/Prediction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Prediction


## Comments

* Prediction is a concept referring to activities or tasks in the context
of technologies producing or using them as inputs or outputs



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Prediction |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Prediction |
| native | tech:Prediction |
| exact | dpv_tech:Prediction, dpv_tech_owl:Prediction |
| close | iso22989:Prediction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Prediction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Prediction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'An inference or prediction of an action or data or decision in the

  context of technologies'
comments:
- 'Prediction is a concept referring to activities or tasks in the context

  of technologies producing or using them as inputs or outputs'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Prediction
exact_mappings:
- dpv_tech:Prediction
- dpv_tech_owl:Prediction
close_mappings:
- iso22989:Prediction
is_a: InputOutput
class_uri: tech:Prediction

```
</details>

### Induced

<details>
```yaml
name: Prediction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Prediction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'An inference or prediction of an action or data or decision in the

  context of technologies'
comments:
- 'Prediction is a concept referring to activities or tasks in the context

  of technologies producing or using them as inputs or outputs'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Prediction
exact_mappings:
- dpv_tech:Prediction
- dpv_tech_owl:Prediction
close_mappings:
- iso22989:Prediction
is_a: InputOutput
class_uri: tech:Prediction

```
</details></div>