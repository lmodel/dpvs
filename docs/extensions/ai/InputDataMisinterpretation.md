---
search:
  boost: 10.0
---

# Class: InputDataMisinterpretation 


_Concept representing input data being misinterpreted_



<div data-search-exclude markdown="1">



URI: [ai:InputDataMisinterpretation](https://w3id.org/lmodel/dpv/ai/InputDataMisinterpretation)





```mermaid
 classDiagram
    class InputDataMisinterpretation
    click InputDataMisinterpretation href "../InputDataMisinterpretation/"
      RiskConcept <|-- InputDataMisinterpretation
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataMisinterpretation
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataMisinterpretation** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataMisinterpretation](https://w3id.org/lmodel/dpv/ai/InputDataMisinterpretation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Misinterpretation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataMisinterpretation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataMisinterpretation |
| native | ai:InputDataMisinterpretation |
| exact | dpv_ai:InputDataMisinterpretation, dpv_ai_owl:InputDataMisinterpretation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being misinterpreted
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Misinterpretation
exact_mappings:
- dpv_ai:InputDataMisinterpretation
- dpv_ai_owl:InputDataMisinterpretation
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataMisinterpretation

```
</details>

### Induced

<details>
```yaml
name: InputDataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being misinterpreted
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Misinterpretation
exact_mappings:
- dpv_ai:InputDataMisinterpretation
- dpv_ai_owl:InputDataMisinterpretation
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataMisinterpretation

```
</details></div>