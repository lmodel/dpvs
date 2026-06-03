---
search:
  boost: 10.0
---

# Class: InputDataSparse 


_Concept representing input data being sparse_



<div data-search-exclude markdown="1">



URI: [ai:InputDataSparse](https://w3id.org/lmodel/dpv/ai/InputDataSparse)





```mermaid
 classDiagram
    class InputDataSparse
    click InputDataSparse href "../InputDataSparse/"
      RiskConcept <|-- InputDataSparse
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataSparse
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataSparse** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataSparse](https://w3id.org/lmodel/dpv/ai/InputDataSparse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Sparse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataSparse |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataSparse |
| native | ai:InputDataSparse |
| exact | dpv_ai:InputDataSparse, dpv_ai_owl:InputDataSparse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being sparse
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Sparse
exact_mappings:
- dpv_ai:InputDataSparse
- dpv_ai_owl:InputDataSparse
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataSparse

```
</details>

### Induced

<details>
```yaml
name: InputDataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being sparse
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Sparse
exact_mappings:
- dpv_ai:InputDataSparse
- dpv_ai_owl:InputDataSparse
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataSparse

```
</details></div>