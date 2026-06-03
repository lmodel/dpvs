---
search:
  boost: 10.0
---

# Class: TestingDataUnverified 


_Concept representing testing data being unverified_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataUnverified](https://w3id.org/lmodel/dpv/ai/TestingDataUnverified)





```mermaid
 classDiagram
    class TestingDataUnverified
    click TestingDataUnverified href "../TestingDataUnverified/"
      RiskConcept <|-- TestingDataUnverified
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataUnverified
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataUnverified** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataUnverified](https://w3id.org/lmodel/dpv/ai/TestingDataUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataUnverified |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataUnverified |
| native | ai:TestingDataUnverified |
| exact | dpv_ai:TestingDataUnverified, dpv_ai_owl:TestingDataUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being unverified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Unverified
exact_mappings:
- dpv_ai:TestingDataUnverified
- dpv_ai_owl:TestingDataUnverified
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataUnverified

```
</details>

### Induced

<details>
```yaml
name: TestingDataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being unverified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Unverified
exact_mappings:
- dpv_ai:TestingDataUnverified
- dpv_ai_owl:TestingDataUnverified
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataUnverified

```
</details></div>