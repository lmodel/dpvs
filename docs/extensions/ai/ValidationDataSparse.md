---
search:
  boost: 10.0
---

# Class: ValidationDataSparse 


_Concept representing validation data being sparse_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataSparse](https://w3id.org/lmodel/dpv/ai/ValidationDataSparse)





```mermaid
 classDiagram
    class ValidationDataSparse
    click ValidationDataSparse href "../ValidationDataSparse/"
      RiskConcept <|-- ValidationDataSparse
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataSparse
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataSparse** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataSparse](https://w3id.org/lmodel/dpv/ai/ValidationDataSparse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Sparse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataSparse |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataSparse |
| native | ai:ValidationDataSparse |
| exact | dpv_ai:ValidationDataSparse, dpv_ai_owl:ValidationDataSparse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being sparse
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Sparse
exact_mappings:
- dpv_ai:ValidationDataSparse
- dpv_ai_owl:ValidationDataSparse
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataSparse

```
</details>

### Induced

<details>
```yaml
name: ValidationDataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being sparse
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Sparse
exact_mappings:
- dpv_ai:ValidationDataSparse
- dpv_ai_owl:ValidationDataSparse
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataSparse

```
</details></div>