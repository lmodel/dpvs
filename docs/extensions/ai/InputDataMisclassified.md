---
search:
  boost: 10.0
---

# Class: InputDataMisclassified 


_Concept representing input data being misclassified_



<div data-search-exclude markdown="1">



URI: [ai:InputDataMisclassified](https://w3id.org/lmodel/dpv/ai/InputDataMisclassified)





```mermaid
 classDiagram
    class InputDataMisclassified
    click InputDataMisclassified href "../InputDataMisclassified/"
      RiskConcept <|-- InputDataMisclassified
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataMisclassified
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataMisclassified** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataMisclassified](https://w3id.org/lmodel/dpv/ai/InputDataMisclassified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Misclassified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataMisclassified |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataMisclassified |
| native | ai:InputDataMisclassified |
| exact | dpv_ai:InputDataMisclassified, dpv_ai_owl:InputDataMisclassified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being misclassified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Misclassified
exact_mappings:
- dpv_ai:InputDataMisclassified
- dpv_ai_owl:InputDataMisclassified
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataMisclassified

```
</details>

### Induced

<details>
```yaml
name: InputDataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being misclassified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Misclassified
exact_mappings:
- dpv_ai:InputDataMisclassified
- dpv_ai_owl:InputDataMisclassified
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataMisclassified

```
</details></div>