---
search:
  boost: 10.0
---

# Class: InputOutput 


_Forms of inputs and outputs associated with a technology_



<div data-search-exclude markdown="1">



URI: [tech:InputOutput](https://w3id.org/lmodel/dpv/tech/InputOutput)





```mermaid
 classDiagram
    class InputOutput
    click InputOutput href "../InputOutput/"
      InputOutput <|-- Content
        click Content href "../Content/"
      InputOutput <|-- DpvAction
        click DpvAction href "../DpvAction/"
      InputOutput <|-- DpvDecision
        click DpvDecision href "../DpvDecision/"
      InputOutput <|-- Input
        click Input href "../Input/"
      InputOutput <|-- Output
        click Output href "../Output/"
      InputOutput <|-- Prediction
        click Prediction href "../Prediction/"
      InputOutput <|-- Recommendation
        click Recommendation href "../Recommendation/"
      
      
```





## Inheritance
* **InputOutput**
    * [DpvAction](DpvAction.md)
    * [DpvDecision](DpvDecision.md)
    * [Input](Input.md)
    * [Output](Output.md)
    * [Prediction](Prediction.md)
    * [Recommendation](Recommendation.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:InputOutput](https://w3id.org/lmodel/dpv/tech/InputOutput) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Input/Output




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#InputOutput |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:InputOutput |
| native | tech:InputOutput |
| exact | dpv_tech:InputOutput, dpv_tech_owl:InputOutput |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputOutput
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#InputOutput
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Forms of inputs and outputs associated with a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Input/Output
exact_mappings:
- dpv_tech:InputOutput
- dpv_tech_owl:InputOutput
class_uri: tech:InputOutput

```
</details>

### Induced

<details>
```yaml
name: InputOutput
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#InputOutput
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Forms of inputs and outputs associated with a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Input/Output
exact_mappings:
- dpv_tech:InputOutput
- dpv_tech_owl:InputOutput
class_uri: tech:InputOutput

```
</details></div>