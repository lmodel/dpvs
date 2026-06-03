---
search:
  boost: 10.0
---

# Class: TestingDataMisclassified 


_Concept representing testing data being misclassified_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataMisclassified](https://w3id.org/lmodel/dpv/ai/TestingDataMisclassified)





```mermaid
 classDiagram
    class TestingDataMisclassified
    click TestingDataMisclassified href "../TestingDataMisclassified/"
      RiskConcept <|-- TestingDataMisclassified
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataMisclassified
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataMisclassified** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataMisclassified](https://w3id.org/lmodel/dpv/ai/TestingDataMisclassified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Misclassified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataMisclassified |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataMisclassified |
| native | ai:TestingDataMisclassified |
| exact | dpv_ai:TestingDataMisclassified, dpv_ai_owl:TestingDataMisclassified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being misclassified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Misclassified
exact_mappings:
- dpv_ai:TestingDataMisclassified
- dpv_ai_owl:TestingDataMisclassified
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataMisclassified

```
</details>

### Induced

<details>
```yaml
name: TestingDataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being misclassified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Misclassified
exact_mappings:
- dpv_ai:TestingDataMisclassified
- dpv_ai_owl:TestingDataMisclassified
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataMisclassified

```
</details></div>