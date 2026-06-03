---
search:
  boost: 10.0
---

# Class: TestingDataSparse 


_Concept representing testing data being sparse_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataSparse](https://w3id.org/lmodel/dpv/ai/TestingDataSparse)





```mermaid
 classDiagram
    class TestingDataSparse
    click TestingDataSparse href "../TestingDataSparse/"
      RiskConcept <|-- TestingDataSparse
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataSparse
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataSparse** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataSparse](https://w3id.org/lmodel/dpv/ai/TestingDataSparse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Sparse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataSparse |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataSparse |
| native | ai:TestingDataSparse |
| exact | dpv_ai:TestingDataSparse, dpv_ai_owl:TestingDataSparse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being sparse
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Sparse
exact_mappings:
- dpv_ai:TestingDataSparse
- dpv_ai_owl:TestingDataSparse
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataSparse

```
</details>

### Induced

<details>
```yaml
name: TestingDataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being sparse
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Sparse
exact_mappings:
- dpv_ai:TestingDataSparse
- dpv_ai_owl:TestingDataSparse
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataSparse

```
</details></div>