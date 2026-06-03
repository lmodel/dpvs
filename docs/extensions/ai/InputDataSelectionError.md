---
search:
  boost: 10.0
---

# Class: InputDataSelectionError 


_Concept representing an error in input data selection_



<div data-search-exclude markdown="1">



URI: [ai:InputDataSelectionError](https://w3id.org/lmodel/dpv/ai/InputDataSelectionError)





```mermaid
 classDiagram
    class InputDataSelectionError
    click InputDataSelectionError href "../InputDataSelectionError/"
      RiskConcept <|-- InputDataSelectionError
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataSelectionError
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataSelectionError** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataSelectionError](https://w3id.org/lmodel/dpv/ai/InputDataSelectionError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Selection Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataSelectionError |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataSelectionError |
| native | ai:InputDataSelectionError |
| exact | dpv_ai:InputDataSelectionError, dpv_ai_owl:InputDataSelectionError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing an error in input data selection
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Selection Error
exact_mappings:
- dpv_ai:InputDataSelectionError
- dpv_ai_owl:InputDataSelectionError
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataSelectionError

```
</details>

### Induced

<details>
```yaml
name: InputDataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing an error in input data selection
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Selection Error
exact_mappings:
- dpv_ai:InputDataSelectionError
- dpv_ai_owl:InputDataSelectionError
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataSelectionError

```
</details></div>